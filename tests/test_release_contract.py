import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'bundle'
def read(name): return json.loads((BUNDLE / name).read_text())

class ReleaseContract(unittest.TestCase):
    def test_optional_agent_is_explicit_foreground_and_read_only(self):
        manifest = read('manifest.json')
        self.assertEqual(manifest['version'], '0.1.1')
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

    def test_editor_tools_and_original_pixels_are_unchanged(self):
        prior = json.loads((ROOT / 'review/releases/0.1.0/RELEASE.json').read_text())['release_files_sha256']
        for name in ('main.splash', 'tools.json', 'screenshots/01-preview.png', 'screenshots/02-editor.png'):
            self.assertEqual(hashlib.sha256((BUNDLE / name).read_bytes()).hexdigest(), prior[name], name)

if __name__ == '__main__': unittest.main()
