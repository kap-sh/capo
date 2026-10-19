"""Generated from Smithy shape ``com.amazonaws.iam#ListVirtualMFADevicesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.response_marker_type
    import capo_iam.types.virtual_mfa_device_list_type


class ListVirtualMFADevicesResponse(TypedDict, closed=True):
    virtual_mfa_devices: (
        "capo_iam.types.virtual_mfa_device_list_type.virtualMFADeviceListType"
    )
    """<p> The list of virtual MFA devices in the current account that match the <code>AssignmentStatus</code> value that was passed in the request.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListVirtualMFADevicesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.virtual_mfa_device_list_type

    capo_iam.types.virtual_mfa_device_list_type.serialize_query(
        value["virtual_mfa_devices"], pairs, f"{key_prefix}VirtualMFADevices"
    )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListVirtualMFADevicesResponse:
    out: ListVirtualMFADevicesResponse = {}  # type: ignore[typeddict-item]
    child_virtual_mfa_devices = el.find("VirtualMFADevices")
    if child_virtual_mfa_devices is not None:
        import capo_iam.types.virtual_mfa_device_list_type

        out["virtual_mfa_devices"] = (
            capo_iam.types.virtual_mfa_device_list_type.deserialize_query(
                child_virtual_mfa_devices
            )
        )
    else:
        out["virtual_mfa_devices"] = []
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out


def redact_sensitive(value: ListVirtualMFADevicesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "virtual_mfa_devices" in value:
        import capo_iam.types.virtual_mfa_device_list_type

        out["virtual_mfa_devices"] = (
            capo_iam.types.virtual_mfa_device_list_type.redact_sensitive(
                value["virtual_mfa_devices"]
            )
        )
    return out
