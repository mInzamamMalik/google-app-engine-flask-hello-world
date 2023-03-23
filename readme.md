

`gcloud config set app/cloud_build_timeout 900` (seconds) to increase buildtime limit in flex env, this will not work in standard env, default value 600seconds

deploy: `sudo gcloud app deploy --project read-me-a-story3`

view app in browser: `gcloud app browse --project=read-me-a-story3`
view logs: `gcloud app logs tail -s default`



<hr>

App Engine free quota in free tier
28 hours per day of "F" instances
9 hours per day of "B" instances
1 GB of egress per day
The Google Cloud Free Tier is available only for the Standard Environment.

Learn more (https://cloud.google.com/appengine/pricing)

