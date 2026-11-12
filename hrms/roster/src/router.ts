import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/",
		name: "Home",
		component: () => import("./views/Home.vue"),
	},
	{
		path: "/desk/hr-setup",
		name: "HRSetup",
		component: () => import("./views/HRSetup.vue"),
	},
	{
		path: "/app/hr-setup",
		redirect: "/desk/hr-setup",
	},
	{
		path: "/hr-setup",
		redirect: "/desk/hr-setup",
	},
	{
		path: "/hr/roster",
		redirect: "/",
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
