"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.application_component
    import capo_application_insights.types.resource_list


class DescribeComponentResponse(TypedDict, closed=True):
    application_component: NotRequired[
        "capo_application_insights.types.application_component.ApplicationComponent"
    ]
    resource_list: NotRequired[
        "capo_application_insights.types.resource_list.ResourceList"
    ]
    """<p>The list of resource ARNs that belong to the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComponentResponse) -> dict:
    out: dict = {}
    if "application_component" in value:
        import capo_application_insights.types.application_component

        out["ApplicationComponent"] = (
            capo_application_insights.types.application_component.serialize_aws_json_1_1(
                value["application_component"]
            )
        )
    if "resource_list" in value:
        import capo_application_insights.types.resource_list

        out["ResourceList"] = (
            capo_application_insights.types.resource_list.serialize_aws_json_1_1(
                value["resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComponentResponse:
    out: DescribeComponentResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationComponent") is not None:
        import capo_application_insights.types.application_component

        out["application_component"] = (
            capo_application_insights.types.application_component.deserialize_aws_json_1_1(
                data["ApplicationComponent"]
            )
        )
    if data.get("ResourceList") is not None:
        import capo_application_insights.types.resource_list

        out["resource_list"] = (
            capo_application_insights.types.resource_list.deserialize_aws_json_1_1(
                data["ResourceList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeComponentResponse) -> dict:
    out: dict = {}
    if "application_component" in value:
        import capo_application_insights.types.application_component

        out["ApplicationComponent"] = (
            capo_application_insights.types.application_component.serialize_cbor(
                value["application_component"]
            )
        )
    if "resource_list" in value:
        import capo_application_insights.types.resource_list

        out["ResourceList"] = (
            capo_application_insights.types.resource_list.serialize_cbor(
                value["resource_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeComponentResponse:
    out: DescribeComponentResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationComponent") is not None:
        import capo_application_insights.types.application_component

        out["application_component"] = (
            capo_application_insights.types.application_component.deserialize_cbor(
                data["ApplicationComponent"]
            )
        )
    if data.get("ResourceList") is not None:
        import capo_application_insights.types.resource_list

        out["resource_list"] = (
            capo_application_insights.types.resource_list.deserialize_cbor(
                data["ResourceList"]
            )
        )
    return out
