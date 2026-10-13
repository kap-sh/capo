"""Generated from Smithy shape ``com.amazonaws.tnb#InstantiateSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.tag_map


class InstantiateSolNetworkInstanceInput(TypedDict, closed=True):
    ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    dry_run: NotRequired["bool"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    additional_params_for_ns: NotRequired["object"]
    """<p>Provides values for the configurable properties.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstantiateSolNetworkInstanceInput) -> dict:
    out: dict = {}
    if "additional_params_for_ns" in value:
        out["additionalParamsForNs"] = value["additional_params_for_ns"]
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> InstantiateSolNetworkInstanceInput:
    out: InstantiateSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("additionalParamsForNs") is not None:
        out["additional_params_for_ns"] = data["additionalParamsForNs"]
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: InstantiateSolNetworkInstanceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
