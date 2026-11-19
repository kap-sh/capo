"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormTrait``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.rx_norm_trait_name


class RxNormTrait(TypedDict, closed=True):
    name: NotRequired["capo_comprehendmedical.types.rx_norm_trait_name.RxNormTraitName"]
    """<p>Provides a name or contextual description about the trait.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected trait.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehendmedical.types.rx_norm_trait_name

        out["Name"] = (
            capo_comprehendmedical.types.rx_norm_trait_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormTrait:
    out: RxNormTrait = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_name

        out["name"] = (
            capo_comprehendmedical.types.rx_norm_trait_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehendmedical.types.rx_norm_trait_name

        out["Name"] = capo_comprehendmedical.types.rx_norm_trait_name.serialize_cbor(
            value["name"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> RxNormTrait:
    out: RxNormTrait = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehendmedical.types.rx_norm_trait_name

        out["name"] = capo_comprehendmedical.types.rx_norm_trait_name.deserialize_cbor(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
