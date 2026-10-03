"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PolicyDocument``."""

from typing import TypeAlias

"""A resource policy document, as a JSON string. The "default" policy can be up to 20 KB (20,480 bytes of UTF-8) by default. This quota is adjustable in Service Quotas. A "default" policy that exceeds the quota is rejected with PolicyLengthExceededException. No policy document can exceed 389,120 bytes of UTF-8, regardless of the quota."""
PolicyDocument: TypeAlias = str
