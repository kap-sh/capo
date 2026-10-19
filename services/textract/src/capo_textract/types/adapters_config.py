"""Generated from Smithy shape ``com.amazonaws.textract#AdaptersConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapters


class AdaptersConfig(TypedDict, closed=True):
    adapters: "capo_textract.types.adapters.Adapters"
    """<p>A list of adapters to be used when analyzing the specified document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdaptersConfig) -> dict:
    out: dict = {}
    import capo_textract.types.adapters

    out["Adapters"] = capo_textract.types.adapters.serialize_aws_json_1_1(
        value["adapters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdaptersConfig:
    out: AdaptersConfig = {}  # type: ignore[typeddict-item]
    if data.get("Adapters") is not None:
        import capo_textract.types.adapters

        out["adapters"] = capo_textract.types.adapters.deserialize_aws_json_1_1(
            data["Adapters"]
        )
    else:
        out["adapters"] = []
    return out
