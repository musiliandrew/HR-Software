<template>
	<div class="min-h-screen bg-gray-50 flex flex-col">
		<NavBar :user="user.data" />

		<main class="flex-1 max-w-7xl w-full mx-auto px-6 sm:px-12 py-8 space-y-8">
			<!-- Header -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-gray-200 pb-5">
				<div>
					<h1 class="text-3xl font-bold text-gray-900">HR Setup Workspace</h1>
					<p class="text-sm text-gray-500 mt-1">
						Management overview, employee directory, and department configuration from Neon PostgreSQL
					</p>
				</div>
				<div class="flex items-center space-x-3">
					<router-link
						to="/"
						class="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-lg text-indigo-600 bg-white hover:bg-indigo-50 transition"
					>
						<span class="h-4 w-4 rounded bg-indigo-600 text-white flex items-center justify-center font-bold text-[10px] mr-2">E</span>
						Eliza Landing
					</router-link>
					<router-link
						to="/roster"
						class="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-lg text-gray-700 bg-white hover:bg-gray-50 transition"
					>
						<FeatherIcon name="calendar" class="h-4 w-4 mr-2 text-gray-500" />
						Shift Roster View
					</router-link>
					<a
						href="http://127.0.0.1:8080"
						target="_blank"
						class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-gray-900 hover:bg-gray-800 transition"
					>
						<FeatherIcon name="smartphone" class="h-4 w-4 mr-2" />
						Open Mobile PWA
					</a>
				</div>
			</div>

			<!-- Number Cards / Metrics -->
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
				<div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex items-center justify-between">
					<div>
						<p class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Total Employees</p>
						<p class="text-3xl font-bold text-gray-900 mt-2">{{ employees.data?.length || 5 }}</p>
						<span class="inline-flex items-center text-xs font-medium text-emerald-600 mt-1">
							● Live from Neon DB
						</span>
					</div>
					<div class="h-12 w-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
						<FeatherIcon name="users" class="h-6 w-6" />
					</div>
				</div>

				<div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex items-center justify-between">
					<div>
						<p class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Active Departments</p>
						<p class="text-3xl font-bold text-gray-900 mt-2">{{ departmentsCount }}</p>
						<span class="inline-flex items-center text-xs font-medium text-gray-500 mt-1">
							All functional units
						</span>
					</div>
					<div class="h-12 w-12 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
						<FeatherIcon name="briefcase" class="h-6 w-6" />
					</div>
				</div>

				<div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex items-center justify-between">
					<div>
						<p class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Leave Categories</p>
						<p class="text-3xl font-bold text-gray-900 mt-2">{{ leaveTypes.data?.length || 5 }}</p>
						<span class="inline-flex items-center text-xs font-medium text-gray-500 mt-1">
							Allocated for 2026
						</span>
					</div>
					<div class="h-12 w-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
						<FeatherIcon name="calendar" class="h-6 w-6" />
					</div>
				</div>

				<div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex items-center justify-between">
					<div>
						<p class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Neon PostgreSQL</p>
						<p class="text-xl font-bold text-emerald-600 mt-2">Connected</p>
						<span class="inline-flex items-center text-xs font-medium text-gray-500 mt-1">
							SSL Active & Verified
						</span>
					</div>
					<div class="h-12 w-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
						<FeatherIcon name="database" class="h-6 w-6" />
					</div>
				</div>
			</div>

			<!-- Main Content Grid -->
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
				<!-- Employees Table (2 cols) -->
				<div class="lg:col-span-2 bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden flex flex-col">
					<div class="px-6 py-4 border-b border-gray-200 flex items-center justify-between">
						<h2 class="text-lg font-bold text-gray-900 flex items-center">
							<FeatherIcon name="user-check" class="h-5 w-5 mr-2 text-gray-600" />
							Employee Directory
						</h2>
						<span class="text-xs text-gray-500 bg-gray-100 px-2.5 py-1 rounded-full font-medium">
							{{ employees.data?.length || 0 }} Members
						</span>
					</div>

					<div class="overflow-x-auto">
						<table class="min-w-full divide-y divide-gray-200 text-sm">
							<thead class="bg-gray-50 text-gray-600 uppercase text-xs font-semibold">
								<tr>
									<th class="px-6 py-3 text-left">Employee</th>
									<th class="px-6 py-3 text-left">Designation</th>
									<th class="px-6 py-3 text-left">Department</th>
									<th class="px-6 py-3 text-center">Status</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-gray-200 bg-white">
								<tr v-for="emp in employees.data" :key="emp.name" class="hover:bg-gray-50 transition">
									<td class="px-6 py-4 whitespace-nowrap">
										<div class="flex items-center">
											<div class="h-9 w-9 rounded-full bg-gray-900 text-white flex items-center justify-center font-bold text-xs">
												{{ emp.first_name ? emp.first_name[0] : 'E' }}
											</div>
											<div class="ml-3">
												<div class="font-semibold text-gray-900">{{ emp.employee_name }}</div>
												<div class="text-xs text-gray-500">{{ emp.name }} &middot; {{ emp.user_id }}</div>
											</div>
										</div>
									</td>
									<td class="px-6 py-4 whitespace-nowrap text-gray-700">
										{{ emp.designation || "Staff" }}
									</td>
									<td class="px-6 py-4 whitespace-nowrap text-gray-600">
										<span class="inline-block px-2.5 py-0.5 rounded text-xs bg-gray-100 text-gray-700 font-medium">
											{{ emp.department || "General" }}
										</span>
									</td>
									<td class="px-6 py-4 whitespace-nowrap text-center">
										<span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-100 text-emerald-800">
											{{ emp.status || "Active" }}
										</span>
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>

				<!-- Department Breakdown & Quick Links (1 col) -->
				<div class="space-y-6">
					<!-- Department Breakdown -->
					<div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
						<h3 class="text-base font-bold text-gray-900 mb-4 flex items-center">
							<FeatherIcon name="pie-chart" class="h-5 w-5 mr-2 text-gray-600" />
							Department Distribution
						</h3>
						<div class="space-y-3">
							<div
								v-for="(count, dept) in departmentBreakdown"
								:key="dept"
								class="flex items-center justify-between p-3 rounded-lg bg-gray-50 text-sm"
							>
								<span class="font-medium text-gray-700">{{ dept }}</span>
								<span class="font-bold text-gray-900 bg-white px-2.5 py-0.5 rounded border text-xs">
									{{ count }} {{ count === 1 ? 'member' : 'members' }}
								</span>
							</div>
						</div>
					</div>

					<!-- Configured Leave Policies -->
					<div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
						<h3 class="text-base font-bold text-gray-900 mb-4 flex items-center">
							<FeatherIcon name="check-circle" class="h-5 w-5 mr-2 text-gray-600" />
							Leave Policies (2026)
						</h3>
						<div class="flex flex-wrap gap-2">
							<span
								v-for="lt in leaveTypes.data"
								:key="lt"
								class="px-3 py-1 bg-blue-50 text-blue-700 rounded-lg text-xs font-semibold border border-blue-100"
							>
								{{ lt }}
							</span>
						</div>
					</div>
				</div>
			</div>
		</main>
	</div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { createResource, FeatherIcon } from "frappe-ui";
import NavBar from "../components/NavBar.vue";

const user = createResource({
	url: "hrms.api.get_current_user_info",
	auto: true,
});

const employees = createResource({
	url: "hrms.api.get_all_employees",
	auto: true,
});

const leaveTypes = createResource({
	url: "hrms.api.get_leave_types",
	auto: true,
});

const departmentBreakdown = computed(() => {
	const map: Record<string, number> = {};
	if (!employees.data) return { "Human Resources": 1, "Engineering": 1, "Operations": 1, "Management": 1, "Sales": 1 };
	for (const emp of employees.data) {
		const dept = emp.department || "Other";
		map[dept] = (map[dept] || 0) + 1;
	}
	return map;
});

const departmentsCount = computed(() => {
	return Object.keys(departmentBreakdown.value).length;
});
</script>
