"""Generated from Smithy shape ``com.amazonaws.s3control#AsyncRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.create_multi_region_access_point_input
    import capo_s3_control.types.delete_multi_region_access_point_input
    import capo_s3_control.types.put_multi_region_access_point_policy_input


class AsyncRequestParameters(TypedDict, closed=True):
    create_multi_region_access_point_request: NotRequired[
        "capo_s3_control.types.create_multi_region_access_point_input.CreateMultiRegionAccessPointInput"
    ]
    """<p>A container of the parameters for a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html">CreateMultiRegionAccessPoint</a> request.</p>"""
    delete_multi_region_access_point_request: NotRequired[
        "capo_s3_control.types.delete_multi_region_access_point_input.DeleteMultiRegionAccessPointInput"
    ]
    """<p>A container of the parameters for a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html">DeleteMultiRegionAccessPoint</a> request.</p>"""
    put_multi_region_access_point_policy_request: NotRequired[
        "capo_s3_control.types.put_multi_region_access_point_policy_input.PutMultiRegionAccessPointPolicyInput"
    ]
    """<p>A container of the parameters for a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPoint.html">PutMultiRegionAccessPoint</a> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AsyncRequestParameters, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "create_multi_region_access_point_request" in value:
        import capo_s3_control.types.create_multi_region_access_point_input

        capo_s3_control.types.create_multi_region_access_point_input.serialize_xml(
            value["create_multi_region_access_point_request"],
            el,
            "CreateMultiRegionAccessPointRequest",
        )
    if "delete_multi_region_access_point_request" in value:
        import capo_s3_control.types.delete_multi_region_access_point_input

        capo_s3_control.types.delete_multi_region_access_point_input.serialize_xml(
            value["delete_multi_region_access_point_request"],
            el,
            "DeleteMultiRegionAccessPointRequest",
        )
    if "put_multi_region_access_point_policy_request" in value:
        import capo_s3_control.types.put_multi_region_access_point_policy_input

        capo_s3_control.types.put_multi_region_access_point_policy_input.serialize_xml(
            value["put_multi_region_access_point_policy_request"],
            el,
            "PutMultiRegionAccessPointPolicyRequest",
        )


def deserialize_xml(el: Element) -> AsyncRequestParameters:
    out: AsyncRequestParameters = {}  # type: ignore[typeddict-item]
    child_create_multi_region_access_point_request = el.find(
        "CreateMultiRegionAccessPointRequest"
    )
    if child_create_multi_region_access_point_request is not None:
        import capo_s3_control.types.create_multi_region_access_point_input

        out["create_multi_region_access_point_request"] = (
            capo_s3_control.types.create_multi_region_access_point_input.deserialize_xml(
                child_create_multi_region_access_point_request
            )
        )
    child_delete_multi_region_access_point_request = el.find(
        "DeleteMultiRegionAccessPointRequest"
    )
    if child_delete_multi_region_access_point_request is not None:
        import capo_s3_control.types.delete_multi_region_access_point_input

        out["delete_multi_region_access_point_request"] = (
            capo_s3_control.types.delete_multi_region_access_point_input.deserialize_xml(
                child_delete_multi_region_access_point_request
            )
        )
    child_put_multi_region_access_point_policy_request = el.find(
        "PutMultiRegionAccessPointPolicyRequest"
    )
    if child_put_multi_region_access_point_policy_request is not None:
        import capo_s3_control.types.put_multi_region_access_point_policy_input

        out["put_multi_region_access_point_policy_request"] = (
            capo_s3_control.types.put_multi_region_access_point_policy_input.deserialize_xml(
                child_put_multi_region_access_point_policy_request
            )
        )
    return out
