"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeConstraintOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_detail
    import capo_service_catalog.types.constraint_parameters
    import capo_service_catalog.types.status


class DescribeConstraintOutput(TypedDict, closed=True):
    constraint_detail: NotRequired[
        "capo_service_catalog.types.constraint_detail.ConstraintDetail"
    ]
    """<p>Information about the constraint.</p>"""
    constraint_parameters: NotRequired[
        "capo_service_catalog.types.constraint_parameters.ConstraintParameters"
    ]
    """<p>The constraint parameters.</p>"""
    status: NotRequired["capo_service_catalog.types.status.Status"]
    """<p>The status of the current request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConstraintOutput) -> dict:
    out: dict = {}
    if "constraint_detail" in value:
        import capo_service_catalog.types.constraint_detail

        out["ConstraintDetail"] = (
            capo_service_catalog.types.constraint_detail.serialize_aws_json_1_1(
                value["constraint_detail"]
            )
        )
    if "constraint_parameters" in value:
        out["ConstraintParameters"] = value["constraint_parameters"]
    if "status" in value:
        import capo_service_catalog.types.status

        out["Status"] = capo_service_catalog.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConstraintOutput:
    out: DescribeConstraintOutput = {}  # type: ignore[typeddict-item]
    if data.get("ConstraintDetail") is not None:
        import capo_service_catalog.types.constraint_detail

        out["constraint_detail"] = (
            capo_service_catalog.types.constraint_detail.deserialize_aws_json_1_1(
                data["ConstraintDetail"]
            )
        )
    if data.get("ConstraintParameters") is not None:
        out["constraint_parameters"] = data["ConstraintParameters"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.status

        out["status"] = capo_service_catalog.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConstraintOutput) -> dict:
    out: dict = {}
    if "constraint_detail" in value:
        import capo_service_catalog.types.constraint_detail

        out["ConstraintDetail"] = (
            capo_service_catalog.types.constraint_detail.serialize_cbor(
                value["constraint_detail"]
            )
        )
    if "constraint_parameters" in value:
        out["ConstraintParameters"] = value["constraint_parameters"]
    if "status" in value:
        import capo_service_catalog.types.status

        out["Status"] = capo_service_catalog.types.status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeConstraintOutput:
    out: DescribeConstraintOutput = {}  # type: ignore[typeddict-item]
    if data.get("ConstraintDetail") is not None:
        import capo_service_catalog.types.constraint_detail

        out["constraint_detail"] = (
            capo_service_catalog.types.constraint_detail.deserialize_cbor(
                data["ConstraintDetail"]
            )
        )
    if data.get("ConstraintParameters") is not None:
        out["constraint_parameters"] = data["ConstraintParameters"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.status

        out["status"] = capo_service_catalog.types.status.deserialize_cbor(
            data["Status"]
        )
    return out
