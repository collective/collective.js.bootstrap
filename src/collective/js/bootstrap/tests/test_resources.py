# -*- coding: utf-8 -*-
"""Resources tests for this package."""
from collective.js.bootstrap.testing import COLLECTIVE_JS_BOOTSTRAP_FUNCTIONAL_TESTING
from plone.testing.z2 import Browser

import unittest


class TestResources(unittest.TestCase):
    """Test that resources are availables."""

    layer = COLLECTIVE_JS_BOOTSTRAP_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.browser = Browser(self.portal)

    def test_resource_bootstrap_min_js(self):
        """Test if resource bootstrap.min.js is available."""
        self.browser.open(
            '{0}/{1}'.format(
                self.portal.absolute_url(),
                '++resource++collective.js.bootstrap/js/bootstrap.min.js',
            ),
        )
        self.assertIn('Bootstrap', self.browser.contents)

    def test_resource_bootstrap_min_css(self):
        """Test if resource bootstrap.min.css is available."""
        self.browser.open(
            '{0}/{1}'.format(
                self.portal.absolute_url(),
                '++resource++collective.js.bootstrap/css/bootstrap.min.css',
            ),
        )
        self.assertIn('Bootstrap', self.browser.contents)

    def test_resource_bootstrap_theme_min_css(self):
        """Test if resource bootstrap-theme.min.css is available."""
        self.browser.open(
            '{0}/{1}'.format(
                self.portal.absolute_url(),
                '++resource++collective.js.bootstrap/css/'
                'bootstrap-theme.min.css',
            ),
        )
        self.assertIn('Bootstrap', self.browser.contents)
