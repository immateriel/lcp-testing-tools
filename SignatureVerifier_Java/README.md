NOTE: add "BC" (without the quotes) at the end of the CLI (after "verbose")
in order to select the BouncyCastle crypto provider instead of the default Sun ones.

Windows / MS-DOS command line:

run.bat "./example/cacert.pem" "./example/license.lcpl" verbose

run.bat "./example/lcp.crt" "./example/license2.lcpl" verbose


*nix command line:

chmod a+x run.sh && ./run.sh "./example/cacert.pem" "./example/license.lcpl" verbose

chmod a+x run.sh && ./run.sh "./example/lcp.crt" "./example/license2.lcpl" verbose
