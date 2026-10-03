"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeCreateAccountStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.create_account_request_id


class DescribeCreateAccountStatusRequest(TypedDict, closed=True):
    create_account_request_id: (
        "capo_organizations.types.create_account_request_id.CreateAccountRequestId"
    )
    """<p>Specifies the <code>Id</code> value that uniquely identifies the <code>CreateAccount</code> request. You can get the value from the <code>CreateAccountStatus.Id</code> response in an earlier <a>CreateAccount</a> request, or from the <a>ListCreateAccountStatus</a> operation.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a create account request ID string requires "car-" followed by from 8 to 32 lowercase letters or digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateAccountStatusRequest) -> dict:
    out: dict = {}
    out["CreateAccountRequestId"] = value["create_account_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateAccountStatusRequest:
    out: DescribeCreateAccountStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreateAccountRequestId") is not None:
        out["create_account_request_id"] = data["CreateAccountRequestId"]
    else:
        raise DeserializationError(
            "DescribeCreateAccountStatusRequest.create_account_request_id required"
        )
    return out
