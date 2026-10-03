"""Generated from Smithy shape ``com.amazonaws.deadline#HostConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.host_configuration_script
    import capo_deadline.types.host_configuration_script_timeout_seconds


class HostConfiguration(TypedDict, closed=True):
    script_body: "capo_deadline.types.host_configuration_script.HostConfigurationScript"
    """<p>The text of the script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet. The script runs after a worker enters the <code>STARTING</code> state and before the worker processes tasks.</p> <p>For more information about using the script, see <a href="https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-admin.html">Run scripts as an administrator to configure workers</a> in the <i>Deadline Cloud Developer Guide</i>. </p> <important> <p>The script runs as an administrative user (<code>sudo root</code> on Linux, as an Administrator on Windows). </p> </important>"""
    script_timeout_seconds: "capo_deadline.types.host_configuration_script_timeout_seconds.HostConfigurationScriptTimeoutSeconds"
    """<p>The maximum time that the host configuration can run. If the timeout expires, the worker enters the <code>NOT RESPONDING</code> state and shuts down. You are charged for the time that the worker is running the host configuration script.</p> <note> <p>You should configure your fleet for a maximum of one worker while testing your host configuration script to avoid starting additional workers.</p> </note> <p>The default is 300 seconds (5 minutes).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostConfiguration) -> dict:
    out: dict = {}
    out["scriptBody"] = value["script_body"]
    out["scriptTimeoutSeconds"] = value.get("script_timeout_seconds", 300)
    return out


def deserialize_json(data: dict) -> HostConfiguration:
    out: HostConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scriptBody") is not None:
        out["script_body"] = data["scriptBody"]
    else:
        raise DeserializationError("HostConfiguration.script_body required")
    if data.get("scriptTimeoutSeconds") is not None:
        out["script_timeout_seconds"] = data["scriptTimeoutSeconds"]
    else:
        out["script_timeout_seconds"] = 300
    return out
