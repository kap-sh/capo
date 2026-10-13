"""Generated from Smithy shape ``com.amazonaws.organizations#ListDelegatedAdministratorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.delegated_administrators
    import capo_organizations.types.next_token


class ListDelegatedAdministratorsResponse(TypedDict, closed=True):
    delegated_administrators: NotRequired[
        "capo_organizations.types.delegated_administrators.DelegatedAdministrators"
    ]
    """<p>The list of delegated administrators in your organization.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDelegatedAdministratorsResponse) -> dict:
    out: dict = {}
    if "delegated_administrators" in value:
        import capo_organizations.types.delegated_administrators

        out["DelegatedAdministrators"] = (
            capo_organizations.types.delegated_administrators.serialize_aws_json_1_1(
                value["delegated_administrators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDelegatedAdministratorsResponse:
    out: ListDelegatedAdministratorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DelegatedAdministrators") is not None:
        import capo_organizations.types.delegated_administrators

        out["delegated_administrators"] = (
            capo_organizations.types.delegated_administrators.deserialize_aws_json_1_1(
                data["DelegatedAdministrators"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDelegatedAdministratorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "delegated_administrators" in value:
        import capo_organizations.types.delegated_administrators

        out["delegated_administrators"] = (
            capo_organizations.types.delegated_administrators.redact_sensitive(
                value["delegated_administrators"]
            )
        )
    return out
