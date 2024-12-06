<a className="gh-badge" href="https://datahub.io/core/top-level-domain-names"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

This Data Package contains the delegation details of top-level domains

## Data

The data provided (see `data/top-level-domain-names`) in this package offers a consolidated list of top-level domain (TLD) names by compiling information from the following source:

- [IANA Root Zone Database](http://www.iana.org/domains/root/db)

## Preparation

The data is automatically extracted from "The Internet Assigned Numbers Authority (IANA)" site using a script located at `scripts/process.py`. Dependencies for running this script are listed in `scripts/requirements.txt`.

The data is updated monthly via GitHub Actions, ensuring it stays current without manual intervention.

## Automation

Up-to-date (auto-updates every month) top-level-domain-names dataset could be found on the datahub.io: https://datahub.io/core/top-level-domain-names

## License

These data are made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/
