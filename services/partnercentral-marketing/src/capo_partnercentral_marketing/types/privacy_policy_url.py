"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#PrivacyPolicyUrl``."""

from typing import TypeAlias

r"""The URL of the partner's privacy policy, linked from the footer of every email and landing page of a campaign. <p>`https` with a host, no user info, the default port, and none of `" ' ( ) < > \` or whitespace: it is written into pages and email that are HTML-decoded downstream, so a quote would break out of the link. The pattern is the first check; the service applies the full rule. Never the website URL: a landing page's form collects leads with the partner as data controller, so the link must be a real privacy policy."""
PrivacyPolicyUrl: TypeAlias = str
