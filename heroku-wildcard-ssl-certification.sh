#!/bin/sh
set -e

# NEEDS THE FOLLOWING VARS IN ENV:
# DOMAIN
# CLOUDFLARE_TOKEN
# CLOUDFLARE_ACCOUNT_ID
# HEROKU_API_KEY
# HEROKU_APP

git clone https://github.com/Neilpang/acme.sh.git
cd ./acme.sh

# Force ensures it doesnt fail because of lack of cron
./acme.sh --install --force

# Map to environment variables that the ACME script requires
export CF_Token=$CLOUDFLARE_TOKEN
export CF_Account_ID=$CLOUDFLARE_ACCOUNT_ID

# Generate wildcard certificate (this will take approx 130s)
~/.acme.sh/acme.sh --server letsencrypt --issue -d $DOMAIN  -d "*.$DOMAIN"  --dns dns_cf

# Update the certificate in the live app
heroku certs:update "/app/.acme.sh/$DOMAIN/fullchain.cer" "/app/.acme.sh/$DOMAIN/$DOMAIN.key" --confirm $HEROKU_APP --app $HEROKU_APP