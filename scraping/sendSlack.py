# coding: UTF-8
import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/*****")
slack.notify(text="sendSlack.py")