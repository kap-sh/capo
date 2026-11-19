"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaUngraceful``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.lambda_ungraceful_behavior


class LambdaUngraceful(TypedDict, closed=True):
    behavior: "capo_arc_region_switch.types.lambda_ungraceful_behavior.LambdaUngracefulBehavior"
    """<p>The ungraceful behavior for a Lambda function, which must be set to <code>skip</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaUngraceful) -> dict:
    out: dict = {}
    import capo_arc_region_switch.types.lambda_ungraceful_behavior

    out["behavior"] = (
        capo_arc_region_switch.types.lambda_ungraceful_behavior.serialize_aws_json_1_0(
            value.get("behavior", "skip")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaUngraceful:
    out: LambdaUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.lambda_ungraceful_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.lambda_ungraceful_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "skip"
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaUngraceful) -> dict:
    out: dict = {}
    import capo_arc_region_switch.types.lambda_ungraceful_behavior

    out["behavior"] = (
        capo_arc_region_switch.types.lambda_ungraceful_behavior.serialize_cbor(
            value.get("behavior", "skip")
        )
    )
    return out


def deserialize_cbor(data: dict) -> LambdaUngraceful:
    out: LambdaUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.lambda_ungraceful_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.lambda_ungraceful_behavior.deserialize_cbor(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "skip"
    return out
