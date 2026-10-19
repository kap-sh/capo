"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedQueryResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_protected_query_output_configuration
    import capo_cleanrooms.types.role_arn


class MembershipProtectedQueryResultConfiguration(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.membership_protected_query_output_configuration.MembershipProtectedQueryOutputConfiguration"
    """<p>Configuration for protected query results.</p>"""
    role_arn: NotRequired["capo_cleanrooms.types.role_arn.RoleArn"]
    """<p>The unique ARN for an IAM role that is used by Clean Rooms to write protected query results to the result location, given by the member who can receive results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedQueryResultConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.membership_protected_query_output_configuration

    out["outputConfiguration"] = (
        capo_cleanrooms.types.membership_protected_query_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MembershipProtectedQueryResultConfiguration:
    out: MembershipProtectedQueryResultConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.membership_protected_query_output_configuration

        out["output_configuration"] = (
            capo_cleanrooms.types.membership_protected_query_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["output_configuration"] = capo_cleanrooms.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
