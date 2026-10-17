"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.s3_object


class CodeConfig(TypedDict, closed=True):
    s3_object: "capo_lambda_web.types.s3_object.S3Object"
    """<p>The Amazon S3 location of the deployment artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeConfig) -> dict:
    out: dict = {}
    import capo_lambda_web.types.s3_object

    out["s3Object"] = capo_lambda_web.types.s3_object.serialize_json(value["s3_object"])
    return out


def deserialize_json(data: dict) -> CodeConfig:
    out: CodeConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3Object") is not None:
        import capo_lambda_web.types.s3_object

        out["s3_object"] = capo_lambda_web.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    else:
        raise DeserializationError("CodeConfig.s3_object required")
    return out
