"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#PartnerAddress``."""

from typing import TypeAlias

"""The partner's physical postal address, as one line of plain text: the sender's address that commercial email must carry (CAN-SPAM in the US, CASL in Canada). A registered post office box or private mailbox counts. <p>No markup, line break or control character. Shown in the footer of every email, and as the contact line of a landing page. <p>Sensitive: for a sole trader it is a home address, so it is kept out of logs and CloudTrail events."""
PartnerAddress: TypeAlias = str
