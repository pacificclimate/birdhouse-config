# Development

This `docker compose` is set up for development purposes. It will up a dev instance of `quail` with production settings. All you are required to do is to add the following lines to `birdhouse-config/env.local` running on `marble-dev01`:

```
export BIRDHOUSE_EXTRA_CONF_DIRS="${BIRDHOUSE_CONFIG_DIR}/files/quail/dev-component"

...
export QUAIL_DEV_IMAGE="pcic/quail:[your-tag]"
