<template>
	<div class="h-12 bg-white border-b px-12 flex items-center">
		<div class="flex items-center space-x-2">
			<router-link to="/" class="text-indigo-600 hover:text-indigo-700 font-extrabold flex items-center transition text-sm">
				<span class="h-6 w-6 rounded-md bg-indigo-600 text-white flex items-center justify-center font-black mr-2 text-xs">E</span>
				Eliza
			</router-link>
			<FeatherIcon name="chevron-right" class="h-3.5 w-3.5 text-gray-400" />
			<router-link to="/desk/hr-setup" class="text-gray-700 hover:text-blue-600 font-semibold flex items-center transition text-sm">
				HR Setup
			</router-link>
			<FeatherIcon name="chevron-right" class="h-3.5 w-3.5 text-gray-400" />
			<router-link to="/roster" class="font-medium text-gray-600 hover:text-gray-900 transition text-sm">
				Roster
			</router-link>
		</div>
		<Dropdown
			class="ml-auto"
			:options="[
				{
					label: 'My Account',
					onClick: () => goTo('/me'),
				},
				{
					label: 'Log Out',
					onClick: () => logout.submit(),
				},
				{
					label: 'Switch to Desk',
					onClick: () => goTo('/app'),
				},
			]"
		>
			<Avatar
				:label="props.user?.full_name"
				:image="props.user?.user_image"
				size="lg"
				class="cursor-pointer"
			/>
		</Dropdown>
	</div>
</template>

<script setup lang="ts">
import { FeatherIcon, Dropdown, Avatar, createResource } from "frappe-ui";
import FrappeHRLogo from "../icons/FrappeHRLogo.vue";

import { User } from "../views/Home.vue";
import { goTo, raiseToast } from "../utils";

const props = defineProps<{
	user: User;
}>();

// RESOURCES

const logout = createResource({
	url: "logout",
	onSuccess() {
		goTo("/login");
	},
	onError(error: { messages: string[] }) {
		raiseToast("error", error.messages[0]);
	},
});
</script>
