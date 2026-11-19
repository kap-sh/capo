"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListStackInstancesForProvisionedProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.stack_instances


class ListStackInstancesForProvisionedProductOutput(TypedDict, closed=True):
    stack_instances: NotRequired[
        "capo_service_catalog.types.stack_instances.StackInstances"
    ]
    """<p>List of stack instances.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListStackInstancesForProvisionedProductOutput,
) -> dict:
    out: dict = {}
    if "stack_instances" in value:
        import capo_service_catalog.types.stack_instances

        out["StackInstances"] = (
            capo_service_catalog.types.stack_instances.serialize_aws_json_1_1(
                value["stack_instances"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListStackInstancesForProvisionedProductOutput:
    out: ListStackInstancesForProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("StackInstances") is not None:
        import capo_service_catalog.types.stack_instances

        out["stack_instances"] = (
            capo_service_catalog.types.stack_instances.deserialize_aws_json_1_1(
                data["StackInstances"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListStackInstancesForProvisionedProductOutput) -> dict:
    out: dict = {}
    if "stack_instances" in value:
        import capo_service_catalog.types.stack_instances

        out["StackInstances"] = (
            capo_service_catalog.types.stack_instances.serialize_cbor(
                value["stack_instances"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListStackInstancesForProvisionedProductOutput:
    out: ListStackInstancesForProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("StackInstances") is not None:
        import capo_service_catalog.types.stack_instances

        out["stack_instances"] = (
            capo_service_catalog.types.stack_instances.deserialize_cbor(
                data["StackInstances"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
