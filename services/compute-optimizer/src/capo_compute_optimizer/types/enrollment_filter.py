"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnrollmentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.enrollment_filter_name
    import capo_compute_optimizer.types.filter_values


class EnrollmentFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.enrollment_filter_name.EnrollmentFilterName"
    ]
    """<p>The name of the filter.</p> <p>Specify <code>Status</code> to return accounts with a specific enrollment status (for example, <code>Active</code>).</p>"""
    values: NotRequired["capo_compute_optimizer.types.filter_values.FilterValues"]
    """<p>The value of the filter.</p> <p>The valid values are <code>Active</code>, <code>Inactive</code>, <code>Pending</code>, and <code>Failed</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.enrollment_filter_name

        out["name"] = (
            capo_compute_optimizer.types.enrollment_filter_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnrollmentFilter:
    out: EnrollmentFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.enrollment_filter_name

        out["name"] = (
            capo_compute_optimizer.types.enrollment_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnrollmentFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.enrollment_filter_name

        out["name"] = (
            capo_compute_optimizer.types.enrollment_filter_name.serialize_cbor(
                value["name"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> EnrollmentFilter:
    out: EnrollmentFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.enrollment_filter_name

        out["name"] = (
            capo_compute_optimizer.types.enrollment_filter_name.deserialize_cbor(
                data["name"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.deserialize_cbor(
            data["values"]
        )
    return out
