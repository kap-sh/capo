"""Generated from Smithy shape ``com.amazonaws.autoscaling#AccountSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.ascii_string_max_len255
    import capo_auto_scaling.types.timestamp_type


class AccountSetting(TypedDict, closed=True):
    name: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The name of the account setting. Each account setting has a unique name that identifies the specific feature it controls. </p>"""
    value: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The current value of the account setting. </p>"""
    enforcement_type: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The type of enforcement for the account setting. Valid values include: <code>hard</code> (the setting has a hard enforcement date after which the setting will be enforced and cannot be modified), <code>flexible</code> (the setting has a flexible enforcement where you can always modify the setting value), and <code>none</code> (the setting has no enforcement and can always be modified). </p>"""
    enforcement_date: NotRequired[
        "capo_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p> The date when the account setting will be enforced. After this date, for settings with hard enforcement type, you can no longer modify the setting value. This parameter is only returned for settings with hard or flexible enforcement types. </p>"""
    default_value: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The default value of the account setting before the enforcement date. Valid values are enabled and disabled. This parameter is only returned for settings with hard or flexible enforcement types. </p>"""
    enforced_value: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The value that will be enforced after the enforcement date. Valid values are enabled and disabled. This parameter is only returned for settings with hard or flexible enforcement types. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountSetting, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "enforcement_type" in value:
        pairs.append((f"{key_prefix}EnforcementType", str(value["enforcement_type"])))
    if "enforcement_date" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["enforcement_date"], pairs, f"{key_prefix}EnforcementDate"
        )
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "enforced_value" in value:
        pairs.append((f"{key_prefix}EnforcedValue", str(value["enforced_value"])))


def deserialize_query(el: Element) -> AccountSetting:
    out: AccountSetting = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_enforcement_type = el.find("EnforcementType")
    if child_enforcement_type is not None:
        out["enforcement_type"] = str(child_enforcement_type.text or "")
    child_enforcement_date = el.find("EnforcementDate")
    if child_enforcement_date is not None:
        import capo_auto_scaling.types.timestamp_type

        out["enforcement_date"] = (
            capo_auto_scaling.types.timestamp_type.deserialize_query(
                child_enforcement_date
            )
        )
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_enforced_value = el.find("EnforcedValue")
    if child_enforced_value is not None:
        out["enforced_value"] = str(child_enforced_value.text or "")
    return out
