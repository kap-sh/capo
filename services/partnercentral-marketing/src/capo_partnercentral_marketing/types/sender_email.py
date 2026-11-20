"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SenderEmail``."""

from typing import TypeAlias

r"""The address a campaign's emails are sent from. <p>Its domain — everything after the `@` — must exactly match, ignoring case, the domain of the partner's alliance lead email in AWS Partner Central, and must hold the DKIM and DMARC records `CreateCampaign` names. A subdomain does not match. The shape checks only that there is one `@` with printable-ASCII text either side; the domain and DNS checks are the service's. <p>Printable ASCII, not "anything but whitespace": this becomes the From header of every email the campaign sends, and `\\s` is ASCII-only, so it would admit Unicode separators such as U+2028. Nothing real is lost — Partner Central's lead email and DNS names are ASCII, so a non-ASCII domain could never match. <p>Sensitive: often a person's address, so it is kept out of logs and CloudTrail events."""
SenderEmail: TypeAlias = str
