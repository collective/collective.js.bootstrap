# -*- coding: utf-8 -*-
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.js.bootstrap


class CollectiveJsBootstrapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.js.bootstrap)


COLLECTIVE_JS_BOOTSTRAP_FIXTURE = CollectiveJsBootstrapLayer()


COLLECTIVE_JS_BOOTSTRAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_JS_BOOTSTRAP_FIXTURE,),
    name='CollectiveJsBootstrapLayer:IntegrationTesting',
)


COLLECTIVE_JS_BOOTSTRAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_JS_BOOTSTRAP_FIXTURE,),
    name='CollectiveJsBootstrapLayer:FunctionalTesting',
)


COLLECTIVE_JS_BOOTSTRAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_JS_BOOTSTRAP_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveJsBootstrapLayer:AcceptanceTesting',
)
