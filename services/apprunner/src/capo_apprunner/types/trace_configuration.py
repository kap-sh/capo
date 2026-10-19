"""Generated from Smithy shape ``com.amazonaws.apprunner#TraceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.tracing_vendor


class TraceConfiguration(TypedDict, closed=True):
    vendor: "capo_apprunner.types.tracing_vendor.TracingVendor"
    """<p>The implementation provider chosen for tracing App Runner services.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TraceConfiguration) -> dict:
    out: dict = {}
    import capo_apprunner.types.tracing_vendor

    out["Vendor"] = capo_apprunner.types.tracing_vendor.serialize_aws_json_1_0(
        value["vendor"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TraceConfiguration:
    out: TraceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Vendor") is not None:
        import capo_apprunner.types.tracing_vendor

        out["vendor"] = capo_apprunner.types.tracing_vendor.deserialize_aws_json_1_0(
            data["Vendor"]
        )
    else:
        import typing

        out["vendor"] = typing.cast(
            "capo_apprunner.types.tracing_vendor.TracingVendor", ""
        )
    return out
