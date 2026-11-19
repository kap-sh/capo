"""Generated from Smithy shape ``com.amazonaws.appstream#UserControlMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The user control mode for agent sessions.</p> <ul> <li> <p>VIEW_ONLY - Users can view and observe agent actions as they happen.</p> </li> <li> <p>VIEW_STOP - Users can view agent actions and stop the agent if needed.</p> </li> <li> <p>DISABLED - Users cannot view or stop the agent session.</p> </li> </ul>"""
UserControlMode: TypeAlias = Literal[
    "VIEW_ONLY",
    "VIEW_STOP",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserControlMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserControlMode:
    return cast(UserControlMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserControlMode) -> str:
    return value


def deserialize_cbor(data: str) -> UserControlMode:
    return cast(UserControlMode, data)
