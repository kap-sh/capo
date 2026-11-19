"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolTokenSessionConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.max_sessions_per_user_type


class UserPoolTokenSessionConfigType(TypedDict, closed=True):
    max_per_user: "capo_cognito_identity_provider.types.max_sessions_per_user_type.MaxSessionsPerUserType"
    """<p>The maximum number of active token sessions that a user can have across the user pool. The minimum value is <code>1</code> and the maximum value is <code>100</code>. The default is <code>20</code>. When a user reaches this limit, the next successful authentication automatically evicts that user's least recently used token session before it creates the new session. Lowering this value doesn't evict existing sessions on its own; the user is brought back within the limit on their next sign-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolTokenSessionConfigType) -> dict:
    out: dict = {}
    out["MaxPerUser"] = value["max_per_user"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolTokenSessionConfigType:
    out: UserPoolTokenSessionConfigType = {}  # type: ignore[typeddict-item]
    if data.get("MaxPerUser") is not None:
        out["max_per_user"] = data["MaxPerUser"]
    else:
        out["max_per_user"] = 0
    return out
