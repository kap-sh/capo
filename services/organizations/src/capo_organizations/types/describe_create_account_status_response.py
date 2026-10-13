"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeCreateAccountStatusResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.create_account_status


class DescribeCreateAccountStatusResponse(TypedDict, closed=True):
    create_account_status: NotRequired[
        "capo_organizations.types.create_account_status.CreateAccountStatus"
    ]
    """<p>A structure that contains the current status of an account creation request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateAccountStatusResponse) -> dict:
    out: dict = {}
    if "create_account_status" in value:
        import capo_organizations.types.create_account_status

        out["CreateAccountStatus"] = (
            capo_organizations.types.create_account_status.serialize_aws_json_1_1(
                value["create_account_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateAccountStatusResponse:
    out: DescribeCreateAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("CreateAccountStatus") is not None:
        import capo_organizations.types.create_account_status

        out["create_account_status"] = (
            capo_organizations.types.create_account_status.deserialize_aws_json_1_1(
                data["CreateAccountStatus"]
            )
        )
    return out


def redact_sensitive(value: DescribeCreateAccountStatusResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "create_account_status" in value:
        import capo_organizations.types.create_account_status

        out["create_account_status"] = (
            capo_organizations.types.create_account_status.redact_sensitive(
                value["create_account_status"]
            )
        )
    return out
