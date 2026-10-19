"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogGroupNameConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.log_group_name_pattern


class LogGroupNameConfiguration(TypedDict, closed=True):
    log_group_name_pattern: (
        "capo_observabilityadmin.types.log_group_name_pattern.LogGroupNamePattern"
    )
    """<p>The pattern used to generate destination log group names during centralization. The pattern can contain static text and dynamic variables that are replaced with source attributes. If a variable cannot be resolved, it inherits the value from its parent variable in the hierarchy. The pattern must be between 1 and 512 characters.</p> <p>Supported variables:</p> <ul> <li> <p> <b>${source.logGroup}</b> — The original log group name from the source account.</p> </li> <li> <p> <b>${source.accountId}</b> — The Amazon Web Services account ID where the log originated.</p> </li> <li> <p> <b>${source.region}</b> — The Amazon Web Services Region where the log originated.</p> </li> <li> <p> <b>${source.org.id}</b> — The Amazon Web Services Organization ID of the source account.</p> </li> <li> <p> <b>${source.org.ouId}</b> — The organizational unit ID of the source account.</p> </li> <li> <p> <b>${source.org.rootId}</b> — The organization Root ID.</p> </li> <li> <p> <b>${source.org.path}</b> — The organizational path from account to root.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupNameConfiguration) -> dict:
    out: dict = {}
    out["LogGroupNamePattern"] = value["log_group_name_pattern"]
    return out


def deserialize_json(data: dict) -> LogGroupNameConfiguration:
    out: LogGroupNameConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupNamePattern") is not None:
        out["log_group_name_pattern"] = data["LogGroupNamePattern"]
    else:
        out["log_group_name_pattern"] = ""
    return out
