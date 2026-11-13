<template>
	<header class="h-14 bg-white border-b border-stone-200 px-6 sm:px-12 flex items-center justify-between font-sans">
		<div class="flex items-center space-x-3 text-sm">
			<router-link to="/" class="flex items-center hover:opacity-85 transition">
				<img src="/eliza-logo-dark.png" alt="Eliza HR" class="h-6 w-auto object-contain" />
			</router-link>
			<span class="text-stone-300">/</span>
			<router-link to="/desk/hr-setup" class="font-medium text-stone-900 hover:text-stone-600 transition">
				HR Operations
			</router-link>
			<span class="text-stone-300">/</span>
			<router-link to="/roster" class="font-medium text-stone-500 hover:text-stone-900 transition">
				Shift Roster
			</router-link>
		</div>

		<div class="flex items-center space-x-3">
			<a
				href="http://127.0.0.1:8080"
				target="_blank"
				class="hidden sm:inline-flex items-center px-3 py-1.5 text-xs font-medium rounded-md text-stone-700 bg-stone-100 hover:bg-stone-200 border border-stone-200 transition"
			>
				Employee PWA
			</a>

			<Dropdown
				:options="[
					{
						label: 'Company Overview',
						onClick: () => goTo('/desk/hr-setup'),
					},
					{
						label: 'Shift Roster',
						onClick: () => goTo('/roster'),
					},
					{
						label: 'Landing Page',
						onClick: () => goTo('/'),
					},
					{
						label: 'Log Out',
						onClick: () => logout.submit(),
					},
				]"
			>
				<div class="flex items-center space-x-2 cursor-pointer p-1 rounded-md hover:bg-stone-100 transition">
					<Avatar
						:label="props.user?.full_name || 'Admin'"
						:image="props.user?.user_image"
						size="md"
					/>
					<span class="text-xs font-medium text-stone-800 hidden md:inline">
						{{ props.user?.full_name || 'Administrator' }}
					</span>
				</div>
			</Dropdown>
		</div>
	</header>
</template>

<script setup lang="ts">
import { Dropdown, Avatar, createResource } from "frappe-ui";
import { User } from "../views/Home.vue";
import { goTo, raiseToast } from "../utils";

const props = defineProps<{
	user?: User;
}>();

// RESOURCES
const logout = createResource({
	url: "logout",
	onSuccess() {
		goTo("/");
	},
	onError(error: { messages: string[] }) {
		raiseToast("error", error.messages[0]);
	},
});
</script>
