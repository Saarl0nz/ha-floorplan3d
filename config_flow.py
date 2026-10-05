"""Einrichtung über die Oberfläche."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import CONF_TITLE, DEFAULT_TITLE, DOMAIN


class Floorplan3dConfigFlow(ConfigFlow, domain=DOMAIN):
    """Ein Eintrag genügt: er legt das Panel in der Seitenleiste an."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:
            title = user_input.get(CONF_TITLE) or DEFAULT_TITLE
            return self.async_create_entry(title=title, data={CONF_TITLE: title})
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_TITLE, default=DEFAULT_TITLE): str}
            ),
        )
