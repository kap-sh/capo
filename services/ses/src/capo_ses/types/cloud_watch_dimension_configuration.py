"""Generated from Smithy shape ``com.amazonaws.ses#CloudWatchDimensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.default_dimension_value
    import capo_ses.types.dimension_name
    import capo_ses.types.dimension_value_source


class CloudWatchDimensionConfiguration(TypedDict, closed=True):
    dimension_name: "capo_ses.types.dimension_name.DimensionName"
    """<p>The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""
    dimension_value_source: "capo_ses.types.dimension_value_source.DimensionValueSource"
    """<p>The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an <code>X-SES-MESSAGE-TAGS</code> header or a parameter to the <code>SendEmail</code>/<code>SendRawEmail</code> API, specify <code>messageTag</code>. To use your own email headers, specify <code>emailHeader</code>. To put a custom tag on any link included in your email, specify <code>linkTag</code>.</p>"""
    default_dimension_value: (
        "capo_ses.types.default_dimension_value.DefaultDimensionValue"
    )
    """<p>The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchDimensionConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DimensionName", str(value["dimension_name"])))
    import capo_ses.types.dimension_value_source

    capo_ses.types.dimension_value_source.serialize_query(
        value["dimension_value_source"], pairs, f"{key_prefix}DimensionValueSource"
    )
    pairs.append(
        (f"{key_prefix}DefaultDimensionValue", str(value["default_dimension_value"]))
    )


def deserialize_query(el: Element) -> CloudWatchDimensionConfiguration:
    out: CloudWatchDimensionConfiguration = {}  # type: ignore[typeddict-item]
    child_dimension_name = el.find("DimensionName")
    if child_dimension_name is not None:
        out["dimension_name"] = str(child_dimension_name.text or "")
    else:
        out["dimension_name"] = ""
    child_dimension_value_source = el.find("DimensionValueSource")
    if child_dimension_value_source is not None:
        import capo_ses.types.dimension_value_source

        out["dimension_value_source"] = (
            capo_ses.types.dimension_value_source.deserialize_query(
                child_dimension_value_source
            )
        )
    else:
        import typing

        out["dimension_value_source"] = typing.cast(
            "capo_ses.types.dimension_value_source.DimensionValueSource", ""
        )
    child_default_dimension_value = el.find("DefaultDimensionValue")
    if child_default_dimension_value is not None:
        out["default_dimension_value"] = str(child_default_dimension_value.text or "")
    else:
        out["default_dimension_value"] = ""
    return out
