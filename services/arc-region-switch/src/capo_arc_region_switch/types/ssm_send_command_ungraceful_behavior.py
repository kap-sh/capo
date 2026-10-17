"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmSendCommandUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

"""<p>The ungraceful behavior for an AWS Systems Manager <code>SendCommand</code> execution block, which must be set to <code>skip</code>.</p>"""
SsmSendCommandUngracefulBehavior: TypeAlias = Literal["skip",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmSendCommandUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SsmSendCommandUngracefulBehavior:
    return cast(SsmSendCommandUngracefulBehavior, data)
