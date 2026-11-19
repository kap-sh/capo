"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PartialFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.exception_type
    import capo_cloudwatch.types.failure_code
    import capo_cloudwatch.types.failure_description
    import capo_cloudwatch.types.failure_resource


class PartialFailure(TypedDict, closed=True):
    failure_resource: NotRequired[
        "capo_cloudwatch.types.failure_resource.FailureResource"
    ]
    """<p>The specified rule that could not be deleted.</p>"""
    exception_type: NotRequired["capo_cloudwatch.types.exception_type.ExceptionType"]
    """<p>The type of error.</p>"""
    failure_code: NotRequired["capo_cloudwatch.types.failure_code.FailureCode"]
    """<p>The code of the error.</p>"""
    failure_description: NotRequired[
        "capo_cloudwatch.types.failure_description.FailureDescription"
    ]
    """<p>A description of the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartialFailure) -> dict:
    out: dict = {}
    if "failure_resource" in value:
        out["FailureResource"] = value["failure_resource"]
    if "exception_type" in value:
        out["ExceptionType"] = value["exception_type"]
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_description" in value:
        out["FailureDescription"] = value["failure_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartialFailure:
    out: PartialFailure = {}  # type: ignore[typeddict-item]
    if data.get("FailureResource") is not None:
        out["failure_resource"] = data["FailureResource"]
    if data.get("ExceptionType") is not None:
        out["exception_type"] = data["ExceptionType"]
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureDescription") is not None:
        out["failure_description"] = data["FailureDescription"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PartialFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "failure_resource" in value:
        pairs.append((f"{key_prefix}FailureResource", str(value["failure_resource"])))
    if "exception_type" in value:
        pairs.append((f"{key_prefix}ExceptionType", str(value["exception_type"])))
    if "failure_code" in value:
        pairs.append((f"{key_prefix}FailureCode", str(value["failure_code"])))
    if "failure_description" in value:
        pairs.append(
            (f"{key_prefix}FailureDescription", str(value["failure_description"]))
        )


def deserialize_query(el: Element) -> PartialFailure:
    out: PartialFailure = {}  # type: ignore[typeddict-item]
    child_failure_resource = el.find("FailureResource")
    if child_failure_resource is not None:
        out["failure_resource"] = str(child_failure_resource.text or "")
    child_exception_type = el.find("ExceptionType")
    if child_exception_type is not None:
        out["exception_type"] = str(child_exception_type.text or "")
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_description = el.find("FailureDescription")
    if child_failure_description is not None:
        out["failure_description"] = str(child_failure_description.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartialFailure) -> dict:
    out: dict = {}
    if "failure_resource" in value:
        out["FailureResource"] = value["failure_resource"]
    if "exception_type" in value:
        out["ExceptionType"] = value["exception_type"]
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_description" in value:
        out["FailureDescription"] = value["failure_description"]
    return out


def deserialize_cbor(data: dict) -> PartialFailure:
    out: PartialFailure = {}  # type: ignore[typeddict-item]
    if data.get("FailureResource") is not None:
        out["failure_resource"] = data["FailureResource"]
    if data.get("ExceptionType") is not None:
        out["exception_type"] = data["ExceptionType"]
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureDescription") is not None:
        out["failure_description"] = data["FailureDescription"]
    return out
