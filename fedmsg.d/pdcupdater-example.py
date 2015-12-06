
config = {
    # Should we turn on the realtime updater?
    'pdcupdater.enabled': True,

    # Credentials to talk to PDC
    'pdcupdater.pdc': {
        'server': 'https://pdc.fedorainfracloud.org/rest_api/v1/',
        'insecure': True,  # Just because we have a self-signed cert in the cloud
        'token': 'AWESOME_SECRET_STRING_GOES_HERE',
        # XXX - getting the token is a bit of a pain, but here's a walk through
        # 1) go to https://pdc.fedorainfracloud.org/ in your browser and login.
        # 2) go to https://pdc.fedorainfracloud.org/rest_api/v1/auth/token/obtain/
        # 3) open up the devtools console in your browser, and find the request for the current page.
        # 4) right click to open a context menu and select 'copy as cURL'
        # 5) paste that into a terminal.  It should have your saml cookie.
        # 6) before hitting enter, edit the command to add the following two options
        #       -H 'Accept: application/json'   # to tell the API you want data
        #       --insecure                      # because we have a self-signed cert
        # 7) the command should print out your token.
    },

    ## Credentials to talk to FAS
    #'pdcupdater.fas': {
    #    'base_url': 'https://admin.fedoraproject.org/accounts',
    #    'username': 'YOUR_USERNAME_GOES_HERE',
    #    'password': 'AWESOME_SECRET_PASSWORD_GOES_HERE',
    #},

    # Koji details
    'pdcupdater.koji_url': 'http://koji.fedoraproject.org/kojihub',

    # Where to find composes
    'pdcupdater.old_composes_url': 'https://kojipkgs.fedoraproject.org/compose/',

    # We have an explicit list of these in the config so we can turn them on
    # and off individually in production if one is causing an issue.
    'pdcupdater.handlers': [
        'pdcupdater.handlers.pkgdb:NewPackageHandler',
        'pdcupdater.handlers.pkgdb:NewPackageBranchHandler',
        'pdcupdater.handlers.compose:NewComposeHandler',
        #'pdcupdater.handlers.buildsys:ImageBuildHandler',
        'pdcupdater.handlers.rpms:NewRPMHandler',
        'pdcupdater.handlers.persons:NewPersonHandler',
    ],

    # Augment the base fedmsg logging config to also handle pdcupdater loggers.
    'logging': dict(
        loggers=dict(
            pdcupdater={
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["console"],
            },
        )
    )
}
