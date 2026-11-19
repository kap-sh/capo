"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.preferred_resource_name
    import capo_compute_optimizer.types.preferred_resource_values


class PreferredResource(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_name.PreferredResourceName"
    ]
    """<p> The type of preferred resource to customize. </p> <note> <p>Compute Optimizer only supports the customization of <code>Ec2InstanceTypes</code>.</p> </note>"""
    include_list: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_values.PreferredResourceValues"
    ]
    """<p> The preferred resource type values to include in the recommendation candidates. You can specify the exact resource type value, such as m5.large, or use wild card expressions, such as m5. If this isn’t specified, all supported resources are included by default. You can specify up to 1000 values in this list. </p>"""
    exclude_list: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_values.PreferredResourceValues"
    ]
    """<p> The preferred resource type values to exclude from the recommendation candidates. If this isn’t specified, all supported resources are included by default. You can specify up to 1000 values in this list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredResource) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "include_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["includeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_aws_json_1_0(
                value["include_list"]
            )
        )
    if "exclude_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["excludeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_aws_json_1_0(
                value["exclude_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreferredResource:
    out: PreferredResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("includeList") is not None:
        import capo_compute_optimizer.types.preferred_resource_values

        out["include_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_aws_json_1_0(
                data["includeList"]
            )
        )
    if data.get("excludeList") is not None:
        import capo_compute_optimizer.types.preferred_resource_values

        out["exclude_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_aws_json_1_0(
                data["excludeList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreferredResource) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.serialize_cbor(
                value["name"]
            )
        )
    if "include_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["includeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_cbor(
                value["include_list"]
            )
        )
    if "exclude_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["excludeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_cbor(
                value["exclude_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PreferredResource:
    out: PreferredResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.deserialize_cbor(
                data["name"]
            )
        )
    if data.get("includeList") is not None:
        import capo_compute_optimizer.types.preferred_resource_values

        out["include_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_cbor(
                data["includeList"]
            )
        )
    if data.get("excludeList") is not None:
        import capo_compute_optimizer.types.preferred_resource_values

        out["exclude_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_cbor(
                data["excludeList"]
            )
        )
    return out
