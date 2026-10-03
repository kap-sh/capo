"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Transform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.expression
    import capo_iotsitewise.types.expression_variables
    import capo_iotsitewise.types.transform_processing_config


class Transform(TypedDict, closed=True):
    expression: "capo_iotsitewise.types.expression.Expression"
    """<p>The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    variables: "capo_iotsitewise.types.expression_variables.ExpressionVariables"
    """<p>The list of variables used in the expression.</p>"""
    processing_config: NotRequired[
        "capo_iotsitewise.types.transform_processing_config.TransformProcessingConfig"
    ]
    """<p>The processing configuration for the given transform property. You can configure transforms to be kept at the edge or forwarded to the Amazon Web Services Cloud. You can also configure transforms to be computed at the edge or in the cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transform) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    import capo_iotsitewise.types.expression_variables

    out["variables"] = capo_iotsitewise.types.expression_variables.serialize_json(
        value["variables"]
    )
    if "processing_config" in value:
        import capo_iotsitewise.types.transform_processing_config

        out["processingConfig"] = (
            capo_iotsitewise.types.transform_processing_config.serialize_json(
                value["processing_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Transform:
    out: Transform = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("Transform.expression required")
    if data.get("variables") is not None:
        import capo_iotsitewise.types.expression_variables

        out["variables"] = capo_iotsitewise.types.expression_variables.deserialize_json(
            data["variables"]
        )
    else:
        raise DeserializationError("Transform.variables required")
    if data.get("processingConfig") is not None:
        import capo_iotsitewise.types.transform_processing_config

        out["processing_config"] = (
            capo_iotsitewise.types.transform_processing_config.deserialize_json(
                data["processingConfig"]
            )
        )
    return out
