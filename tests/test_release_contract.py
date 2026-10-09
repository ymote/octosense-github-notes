import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'bundle'
def read(name): return json.loads((BUNDLE / name).read_text())

class ReleaseContract(unittest.TestCase):
    def test_optional_agent_is_explicit_foreground_and_read_only(self):
        manifest = read('manifest.json')
        self.assertTrue(manifest['version'].startswith('0.2.'))
        self.assertEqual(manifest['id'], 'io.github.ymote.githubnotes')
        self.assertIsNone(manifest['integrity'].get('signature'))
        self.assertNotIn('github', manifest['integrity'])
        agent = manifest['agent']
        self.assertEqual(agent['profile'], 'read-only')
        self.assertEqual(agent['tools'], [])
        # hub sign-manifest omits the contract's default false value.
        self.assertFalse(agent.get('background', False))
        self.assertFalse(agent.get('triggers'))
        self.assertEqual(agent['model']['needs'], ['tool_calling'])
        self.assertEqual(agent['instructions'], 'AGENT.md')
        self.assertTrue((BUNDLE / agent['instructions']).is_file())

    def test_own_tools_are_only_private_nonshareable_foreground_reads(self):
        tools = read('tools.json')['tools']
        self.assertEqual({t['host_method'] for t in tools}, {'github.repositories', 'github.files', 'github.read'})
        self.assertEqual(len(tools), 3)
        for tool in tools:
            self.assertEqual(tool['risk'], 'read')
            self.assertTrue(tool['private_data'])
            self.assertFalse(tool['shareable'])
            self.assertFalse(tool['background'])
        self.assertEqual(set(read('manifest.json')['capabilities']), {'storage', 'auth', 'github'})
        self.assertEqual(read('manifest.json')['network']['hosts'], [])

    def test_read_tools_are_unchanged(self):
        prior = json.loads((ROOT / 'review/releases/0.1.0/RELEASE.json').read_text())['release_files_sha256']
        self.assertEqual(hashlib.sha256((BUNDLE / 'tools.json').read_bytes()).hexdigest(), prior['tools.json'])

    def test_script_reaches_only_its_known_host_methods_and_scopes(self):
        # 0.2.2 rewrote the account screen in main.splash. What the script may
        # ask the host for, and the GitHub scopes it requests, did not change.
        source = (BUNDLE / 'main.splash').read_text()
        self.assertEqual(set(re.findall(r'host\.request\("([a-z_.]+)"', source)), {
            'auth.accounts', 'auth.active', 'auth.connect', 'auth.select', 'auth.disconnect',
            'github.repositories', 'github.files', 'github.read', 'github.review_save'})
        self.assertEqual(re.findall(r'scopes = (\[[^\]]*\])', source),
                         ['["read:user", "public_repo"]', '["read:user", "repo"]'])

if __name__ == '__main__': unittest.main()
