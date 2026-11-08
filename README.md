# CBE410 Week 12: Security CI lab

Use only in your own GitHub repository. Requires Python 3.12; create a virtual environment, install `requirements.txt`, then run `python -m pytest -q`, `bandit -r app.py -ll`, and `pip-audit -r requirements.txt`. Dependency audit depends on live vulnerability data and may report newly disclosed issues.

## Student tasks
1. Push baseline and inspect the Actions run; record test/SAST/SCA outcomes.
2. Add `eval(request.args.get('expression','1+1'))` in a new `/calculate` endpoint. Observe the SAST failure (Bandit B307); remove it and use a fixed operation mapping instead. Never expose the intentionally unsafe endpoint to a public service.
3. Add a failing test (`assert client.get('/health').status_code == 201`) and observe the test gate; restore it.
4. Create a feature branch and pull request; observe that the same security job runs before merge.
5. Explain why passing tests, SAST and SCA does not prove the deployed system is secure.
6. Optional: add a `build` job that depends on `security` and uploads a checksum manifest as an artifact. Discuss why a SHA-256 checksum is not a digital signature.

## Signing demonstration (instructor, local only)
```
openssl genpkey -algorithm ed25519 -out demo-private.pem
openssl pkey -in demo-private.pem -pubout -out demo-public.pem
printf 'release candidate\n' > release.txt
openssl pkeyutl -sign -rawin -inkey demo-private.pem -in release.txt -out release.sig
openssl pkeyutl -verify -rawin -pubin -inkey demo-public.pem -in release.txt -sigfile release.sig
```
Change `release.txt` and rerun verify; it should fail. Never commit private keys. This is an educational local signing exercise, not production provenance/attestation.

## Production discussion
Use protected branches, least-privilege job permissions, pinned third-party actions (full commit SHA), OIDC for cloud credentials, isolated runners, environment approvals, SBOM and artifact provenance, and verify signatures before deployment. CI workflow versions shown here are introductory; pin immutable revisions for production.
