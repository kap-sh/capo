"""Generated from Smithy shape ``com.amazonaws.ses#DescribeConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_attribute_list
    import capo_ses.types.configuration_set_name


class DescribeConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set to describe.</p>"""
    configuration_set_attribute_names: NotRequired[
        "capo_ses.types.configuration_set_attribute_list.ConfigurationSetAttributeList"
    ]
    """<p>A list of configuration set attributes to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeConfigurationSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    if "configuration_set_attribute_names" in value:
        import capo_ses.types.configuration_set_attribute_list

        capo_ses.types.configuration_set_attribute_list.serialize_query(
            value["configuration_set_attribute_names"],
            pairs,
            f"{key_prefix}ConfigurationSetAttributeNames",
        )


def deserialize_query(el: Element) -> DescribeConfigurationSetRequest:
    out: DescribeConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_configuration_set_attribute_names = el.find("ConfigurationSetAttributeNames")
    if child_configuration_set_attribute_names is not None:
        import capo_ses.types.configuration_set_attribute_list

        out["configuration_set_attribute_names"] = (
            capo_ses.types.configuration_set_attribute_list.deserialize_query(
                child_configuration_set_attribute_names
            )
        )
    return out
