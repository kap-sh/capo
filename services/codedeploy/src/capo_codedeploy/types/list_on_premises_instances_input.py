"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.registration_status
    import capo_codedeploy.types.tag_filter_list


class ListOnPremisesInstancesInput(TypedDict, closed=True):
    registration_status: NotRequired[
        "capo_codedeploy.types.registration_status.RegistrationStatus"
    ]
    """<p>The registration status of the on-premises instances:</p> <ul> <li> <p> <code>Deregistered</code>: Include deregistered on-premises instances in the resulting list.</p> </li> <li> <p> <code>Registered</code>: Include registered on-premises instances in the resulting list.</p> </li> </ul>"""
    tag_filters: NotRequired["capo_codedeploy.types.tag_filter_list.TagFilterList"]
    """<p>The on-premises instance tags that are used to restrict the on-premises instance names returned.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOnPremisesInstancesInput) -> dict:
    out: dict = {}
    if "registration_status" in value:
        import capo_codedeploy.types.registration_status

        out["registrationStatus"] = (
            capo_codedeploy.types.registration_status.serialize_aws_json_1_1(
                value["registration_status"]
            )
        )
    if "tag_filters" in value:
        import capo_codedeploy.types.tag_filter_list

        out["tagFilters"] = (
            capo_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(
                value["tag_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOnPremisesInstancesInput:
    out: ListOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("registrationStatus") is not None:
        import capo_codedeploy.types.registration_status

        out["registration_status"] = (
            capo_codedeploy.types.registration_status.deserialize_aws_json_1_1(
                data["registrationStatus"]
            )
        )
    if data.get("tagFilters") is not None:
        import capo_codedeploy.types.tag_filter_list

        out["tag_filters"] = (
            capo_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(
                data["tagFilters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOnPremisesInstancesInput) -> dict:
    out: dict = {}
    if "registration_status" in value:
        import capo_codedeploy.types.registration_status

        out["registrationStatus"] = (
            capo_codedeploy.types.registration_status.serialize_cbor(
                value["registration_status"]
            )
        )
    if "tag_filters" in value:
        import capo_codedeploy.types.tag_filter_list

        out["tagFilters"] = capo_codedeploy.types.tag_filter_list.serialize_cbor(
            value["tag_filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListOnPremisesInstancesInput:
    out: ListOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("registrationStatus") is not None:
        import capo_codedeploy.types.registration_status

        out["registration_status"] = (
            capo_codedeploy.types.registration_status.deserialize_cbor(
                data["registrationStatus"]
            )
        )
    if data.get("tagFilters") is not None:
        import capo_codedeploy.types.tag_filter_list

        out["tag_filters"] = capo_codedeploy.types.tag_filter_list.deserialize_cbor(
            data["tagFilters"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
