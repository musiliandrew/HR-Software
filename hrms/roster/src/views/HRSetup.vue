<template>
	<div class="min-h-screen bg-[#f6f4ef] text-[#1a1a1a] flex flex-col font-sans">
		<NavBar :user="user.data" />

		<main class="flex-1 max-w-7xl w-full mx-auto px-6 sm:px-12 py-8 space-y-8">
			<!-- Workspace Header -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-[#dedbd3] pb-6">
				<div>
					<div class="flex items-center space-x-2">
						<h1 class="text-2xl sm:text-3xl font-semibold tracking-tight text-[#1a1a1a]">
							{{ subscription.data?.company_name || 'Company' }} Workspace
						</h1>
						<span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#e7f2ea] text-[#1f5a3a] border border-[#c2e0cd]">
							{{ subscription.data?.plan_tier || 'Growth' }} Plan
						</span>
					</div>
					<p class="text-sm text-[#6b6a66] mt-1">
						Workforce directory, attendance metrics, department structures, and active company subscription.
					</p>
				</div>

				<div class="flex items-center space-x-3">
					<router-link
						to="/roster"
						class="inline-flex items-center px-4 py-2 border border-[#dedbd3] text-xs font-medium rounded-md text-[#1a1a1a] bg-white hover:bg-[#f6f4ef] transition"
					>
						Shift Roster
					</router-link>
					<a
						href="http://127.0.0.1:8080"
						target="_blank"
						class="inline-flex items-center px-4 py-2 border border-[#dedbd3] text-xs font-medium rounded-md text-[#1a1a1a] bg-white hover:bg-[#f6f4ef] transition"
					>
						Employee PWA
					</a>
					<button
						@click="showAddModal = true"
						class="inline-flex items-center px-4 py-2 text-xs font-medium rounded-md text-[#f6f4ef] bg-[#14110f] hover:opacity-90 transition"
					>
						+ Add Employee
					</button>
				</div>
			</div>

			<!-- Real-World HR Metric Cards (4 Cards) -->
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
				<!-- Card 1: Active Workforce & Seat Capacity -->
				<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-sm flex flex-col justify-between">
					<div class="flex items-center justify-between">
						<span class="text-xs font-medium text-[#6b6a66] uppercase tracking-wider">Total Workforce</span>
						<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
							{{ subscription.data?.plan_tier || 'Growth' }}
						</span>
					</div>
					<div class="mt-3">
						<p class="text-3xl font-semibold text-[#1a1a1a]">
							{{ employees.data?.length || 5 }} <span class="text-sm font-normal text-[#6b6a66]">/ {{ subscription.data?.seat_limit || 50 }} seats</span>
						</p>
						<div class="w-full bg-[#f6f4ef] h-1.5 rounded-full mt-2.5 overflow-hidden border border-[#dedbd3]">
							<div
								class="bg-[#14110f] h-full rounded-full"
								:style="{ width: `${Math.min(100, (((employees.data?.length || 5) / (subscription.data?.seat_limit || 50)) * 100))}%` }"
							></div>
						</div>
					</div>
					<p class="text-xs text-[#6b6a66] mt-3">
						{{ (subscription.data?.seat_limit || 50) - (employees.data?.length || 5) }} seats available for invite
					</p>
				</div>

				<!-- Card 2: On Duty Today -->
				<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-sm flex flex-col justify-between">
					<div class="flex items-center justify-between">
						<span class="text-xs font-medium text-[#6b6a66] uppercase tracking-wider">On Duty Today</span>
						<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-[#e7f2ea] text-[#1f5a3a]">
							● 80% On Site
						</span>
					</div>
					<div class="mt-3">
						<p class="text-3xl font-semibold text-[#1f5a3a]">4 Active</p>
						<p class="text-xs text-[#6b6a66] mt-1">Geo-verified mobile clock-ins</p>
					</div>
					<p class="text-xs text-[#6b6a66] mt-3">
						1 staff scheduled off-shift
					</p>
				</div>

				<!-- Card 3: Pending Approvals -->
				<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-sm flex flex-col justify-between">
					<div class="flex items-center justify-between">
						<span class="text-xs font-medium text-[#6b6a66] uppercase tracking-wider">Pending Requests</span>
						<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-[#fdf3e7] text-[#8a6a43]">
							Action Needed
						</span>
					</div>
					<div class="mt-3">
						<p class="text-3xl font-semibold text-[#8a6a43]">2 to Review</p>
						<p class="text-xs text-[#6b6a66] mt-1">1 Annual leave &middot; 1 Expense claim</p>
					</div>
					<router-link to="/roster" class="text-xs text-[#1a1a1a] font-medium mt-3 hover:underline">
						Review in roster &rarr;
					</router-link>
				</div>

				<!-- Card 4: Monthly Payroll Cycle -->
				<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-sm flex flex-col justify-between">
					<div class="flex items-center justify-between">
						<span class="text-xs font-medium text-[#6b6a66] uppercase tracking-wider">Monthly Payroll</span>
						<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-[#e7f2ea] text-[#1f5a3a]">
							March 2026
						</span>
					</div>
					<div class="mt-3">
						<p class="text-3xl font-semibold text-[#1a1a1a]">$23,500</p>
						<p class="text-xs text-[#6b6a66] mt-1">Base gross & deductions finalized</p>
					</div>
					<p class="text-xs text-[#6b6a66] mt-3">
						Slips distributed to employee mobile PWA
					</p>
				</div>
			</div>

			<!-- Main Content Grid -->
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
				<!-- Left: Employee Directory (2 Cols) -->
				<div class="lg:col-span-2 bg-white rounded-lg border border-[#dedbd3] shadow-sm flex flex-col overflow-hidden">
					<div class="px-6 py-4 border-b border-[#dedbd3] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
						<div class="flex items-center space-x-2">
							<h2 class="text-base font-semibold text-[#1a1a1a]">Employee Directory</h2>
							<span class="text-xs text-[#6b6a66] bg-[#f6f4ef] px-2 py-0.5 rounded border border-[#dedbd3]">
								{{ filteredEmployees.length }} Members
							</span>
						</div>

						<!-- Search Filter -->
						<div class="relative w-full sm:w-64">
							<input
								type="text"
								v-model="searchQuery"
								placeholder="Search name, role, dept..."
								class="w-full text-xs px-3 py-1.5 rounded border border-[#dedbd3] bg-[#f6f4ef] text-[#1a1a1a] placeholder-[#6b6a66] focus:outline-none focus:border-[#14110f]"
							/>
						</div>
					</div>

					<div class="overflow-x-auto">
						<table class="w-full text-left text-xs divide-y divide-[#dedbd3]">
							<thead class="bg-[#f6f4ef] text-[#6b6a66] uppercase font-medium">
								<tr>
									<th class="px-6 py-3">Employee</th>
									<th class="px-6 py-3">Designation</th>
									<th class="px-6 py-3">Department</th>
									<th class="px-6 py-3 text-center">Status</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-[#dedbd3] bg-white text-[#1a1a1a]">
								<tr v-for="emp in filteredEmployees" :key="emp.name" class="hover:bg-[#f6f4ef]/60 transition">
									<td class="px-6 py-3.5 whitespace-nowrap">
										<div class="flex items-center space-x-3">
											<div class="h-8 w-8 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-semibold text-xs">
												{{ emp.first_name ? emp.first_name[0] : (emp.employee_name ? emp.employee_name[0] : 'E') }}
											</div>
											<div>
												<div class="font-medium text-[#1a1a1a]">{{ emp.employee_name }}</div>
												<div class="text-[11px] text-[#6b6a66]">{{ emp.user_id || emp.name }}</div>
											</div>
										</div>
									</td>
									<td class="px-6 py-3.5 whitespace-nowrap text-[#6b6a66]">
										{{ emp.designation || "Staff" }}
									</td>
									<td class="px-6 py-3.5 whitespace-nowrap">
										<span class="inline-block px-2.5 py-0.5 rounded text-[11px] bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
											{{ emp.department || "General" }}
										</span>
									</td>
									<td class="px-6 py-3.5 whitespace-nowrap text-center">
										<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-[#e7f2ea] text-[#1f5a3a]">
											● {{ emp.status || "Active" }}
										</span>
									</td>
								</tr>
								<tr v-if="filteredEmployees.length === 0">
									<td colspan="4" class="px-6 py-8 text-center text-[#6b6a66]">
										No employees found matching "{{ searchQuery }}".
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>

				<!-- Right: Company Overview, Departments & Leave Policies (1 Col) -->
				<div class="space-y-6">
					<!-- Company Subscription Card -->
					<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-sm space-y-4">
						<div class="flex items-center justify-between">
							<h3 class="text-sm font-semibold text-[#1a1a1a]">Company Subscription</h3>
							<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-[#e7f2ea] text-[#1f5a3a]">
								Active
							</span>
						</div>

						<div class="space-y-2 text-xs border-t border-b border-[#dedbd3] py-3 text-[#6b6a66]">
							<div class="flex justify-between">
								<span>Current Plan:</span>
								<strong class="text-[#1a1a1a]">{{ subscription.data?.plan_tier || 'Growth' }} Tier</strong>
							</div>
							<div class="flex justify-between">
								<span>Seat Limit:</span>
								<strong class="text-[#1a1a1a]">{{ subscription.data?.seat_limit || 50 }} Employees</strong>
							</div>
							<div class="flex justify-between">
								<span>Monthly Price:</span>
								<strong class="text-[#1a1a1a]">${{ subscription.data?.monthly_price || 79 }}.00 / mo</strong>
							</div>
							<div class="flex justify-between">
								<span>Billing Contact:</span>
								<strong class="text-[#1a1a1a]">{{ subscription.data?.billing_email || user.data?.email || 'admin@company.com' }}</strong>
							</div>
						</div>

						<button
							@click="showPlanModal = true"
							class="w-full py-2 text-xs font-medium rounded border border-[#dedbd3] bg-[#f6f4ef] hover:bg-white text-[#1a1a1a] transition"
						>
							Change / Upgrade Plan
						</button>
					</div>

					<!-- Department Breakdown -->
					<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-sm">
						<h3 class="text-sm font-semibold text-[#1a1a1a] mb-3">Department Breakdown</h3>
						<div class="space-y-2.5">
							<div
								v-for="(count, dept) in departmentBreakdown"
								:key="dept"
								class="p-2.5 rounded bg-[#f6f4ef] text-xs flex items-center justify-between"
							>
								<span class="font-medium text-[#1a1a1a]">{{ dept }}</span>
								<span class="text-[#6b6a66] font-semibold">
									{{ count }} {{ count === 1 ? 'member' : 'members' }}
								</span>
							</div>
						</div>
					</div>

					<!-- Configured Leave Policies -->
					<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-sm">
						<h3 class="text-sm font-semibold text-[#1a1a1a] mb-3">Leave Categories (2026)</h3>
						<div class="flex flex-wrap gap-1.5">
							<span
								v-for="lt in leaveTypes.data || defaultLeaveTypes"
								:key="lt"
								class="px-2.5 py-1 bg-[#f6f4ef] text-[#1a1a1a] rounded text-[11px] font-medium border border-[#dedbd3]"
							>
								{{ lt }}
							</span>
						</div>
					</div>
				</div>
			</div>
		</main>

		<!-- Add Employee Modal -->
		<div v-if="showAddModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm" @click.self="showAddModal = false">
			<div class="bg-white border border-[#dedbd3] rounded-lg max-w-md w-full p-6 shadow-xl relative text-[#1a1a1a]">
				<button @click="showAddModal = false" class="absolute top-4 right-4 text-[#6b6a66] hover:text-[#1a1a1a] text-lg">&times;</button>
				<h3 class="text-lg font-semibold mb-1">Add Team Member</h3>
				<p class="text-xs text-[#6b6a66] mb-4">
					Employees will receive free self-service access on mobile & web under your company plan.
				</p>

				<div v-if="addError" class="p-2.5 mb-3 rounded bg-red-50 border border-red-200 text-red-700 text-xs">
					{{ addError }}
				</div>

				<form @submit.prevent="submitAddEmployee" class="space-y-3 text-xs">
					<div>
						<label class="block font-medium mb-1 text-[#6b6a66]">Full Name</label>
						<input
							type="text"
							v-model="newEmp.employee_name"
							placeholder="e.g. Michael Scott"
							required
							class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
						/>
					</div>
					<div>
						<label class="block font-medium mb-1 text-[#6b6a66]">Work Email</label>
						<input
							type="email"
							v-model="newEmp.email"
							placeholder="michael@company.com"
							required
							class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
						/>
					</div>
					<div class="grid grid-cols-2 gap-3">
						<div>
							<label class="block font-medium mb-1 text-[#6b6a66]">Department</label>
							<input
								type="text"
								v-model="newEmp.department"
								placeholder="Operations"
								required
								class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
							/>
						</div>
						<div>
							<label class="block font-medium mb-1 text-[#6b6a66]">Designation</label>
							<input
								type="text"
								v-model="newEmp.designation"
								placeholder="Field Supervisor"
								required
								class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
							/>
						</div>
					</div>

					<button
						type="submit"
						:disabled="isSubmittingEmp"
						class="w-full py-2.5 mt-2 rounded bg-[#14110f] text-[#f6f4ef] font-medium text-xs hover:opacity-90 transition disabled:opacity-50"
					>
						{{ isSubmittingEmp ? 'Adding...' : 'Confirm & Add Member' }}
					</button>
				</form>
			</div>
		</div>

		<!-- Change Plan Modal -->
		<div v-if="showPlanModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm" @click.self="showPlanModal = false">
			<div class="bg-white border border-[#dedbd3] rounded-lg max-w-lg w-full p-6 shadow-xl relative text-[#1a1a1a]">
				<button @click="showPlanModal = false" class="absolute top-4 right-4 text-[#6b6a66] hover:text-[#1a1a1a] text-lg">&times;</button>
				<h3 class="text-lg font-semibold mb-1">Company Subscription</h3>
				<p class="text-xs text-[#6b6a66] mb-4">
					The company pays one flat monthly subscription. Select a tier to expand employee seats.
				</p>

				<div class="space-y-3">
					<div
						v-for="plan in plans"
						:key="plan.name"
						@click="selectedPlanTier = plan.name"
						:class="selectedPlanTier === plan.name ? 'border-[#14110f] bg-[#f6f4ef]' : 'border-[#dedbd3] bg-white'"
						class="p-4 rounded-lg border cursor-pointer flex justify-between items-center transition"
					>
						<div>
							<div class="flex items-center space-x-2">
								<strong class="text-sm font-semibold">{{ plan.name }}</strong>
								<span v-if="subscription.data?.plan_tier === plan.name" class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									Current Plan
								</span>
							</div>
							<p class="text-xs text-[#6b6a66] mt-0.5">{{ plan.description }}</p>
							<p class="text-xs font-medium text-[#1a1a1a] mt-1">{{ plan.seats }} Employee Seats</p>
						</div>
						<div class="text-right">
							<span class="text-base font-semibold text-[#1a1a1a]">${{ plan.price }}</span>
							<span class="text-[11px] text-[#6b6a66]">/mo</span>
						</div>
					</div>
				</div>

				<button
					@click="submitPlanChange"
					:disabled="isUpdatingPlan || selectedPlanTier === subscription.data?.plan_tier"
					class="w-full py-2.5 mt-4 rounded bg-[#14110f] text-[#f6f4ef] font-medium text-xs hover:opacity-90 transition disabled:opacity-50"
				>
					{{ isUpdatingPlan ? 'Updating Subscription...' : `Update Plan to ${selectedPlanTier}` }}
				</button>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { createResource } from "frappe-ui";
import NavBar from "../components/NavBar.vue";

const searchQuery = ref("");
const showAddModal = ref(false);
const showPlanModal = ref(false);
const isSubmittingEmp = ref(false);
const isUpdatingPlan = ref(false);
const addError = ref("");
const selectedPlanTier = ref("Growth");

const defaultLeaveTypes = ["Annual Leave", "Sick Leave", "Casual Leave", "Maternity Leave", "Paternity Leave"];

const plans = [
	{ name: "Starter", price: 29, seats: 15, description: "For small teams and growing contractors" },
	{ name: "Growth", price: 79, seats: 50, description: "For scaling teams with shift rostering & geofence tracking" },
	{ name: "Enterprise", price: 199, seats: "Unlimited", description: "Complete workforce automation & dedicated support" },
];

const newEmp = ref({
	employee_name: "",
	email: "",
	department: "Operations",
	designation: "Field Supervisor",
});

// Resources
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

const subscription = createResource({
	url: "saas.get_company_subscription",
	auto: true,
	onSuccess(data: any) {
		if (data?.plan_tier) {
			selectedPlanTier.value = data.plan_tier;
		}
	},
});

// Computeds
const filteredEmployees = computed(() => {
	const list = employees.data || [];
	if (!searchQuery.value.trim()) return list;
	const q = searchQuery.value.toLowerCase();
	return list.filter((emp: any) =>
		(emp.employee_name && emp.employee_name.toLowerCase().includes(q)) ||
		(emp.designation && emp.designation.toLowerCase().includes(q)) ||
		(emp.department && emp.department.toLowerCase().includes(q)) ||
		(emp.user_id && emp.user_id.toLowerCase().includes(q))
	);
});

const departmentBreakdown = computed(() => {
	const map: Record<string, number> = {};
	const list = employees.data || [];
	if (list.length === 0) {
		return { "Management": 1, "Engineering": 1, "Operations": 1, "Human Resources": 1, "Design": 1 };
	}
	for (const emp of list) {
		const dept = emp.department || "General";
		map[dept] = (map[dept] || 0) + 1;
	}
	return map;
});

// Actions
async function submitAddEmployee() {
	isSubmittingEmp.value = true;
	addError.value = "";
	try {
		const res = await fetch("/api/method/saas.invite_employee", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(newEmp.value),
		});
		const result = await res.json();
		if (res.ok) {
			employees.reload();
			subscription.reload();
			showAddModal.value = false;
			newEmp.value = { employee_name: "", email: "", department: "Operations", designation: "Field Supervisor" };
		} else {
			addError.value = result.message || result.error || "Failed to add employee.";
		}
	} catch (err: any) {
		addError.value = err.message || "Network error adding employee.";
	} finally {
		isSubmittingEmp.value = false;
	}
}

async function submitPlanChange() {
	isUpdatingPlan.value = true;
	try {
		const res = await fetch("/api/method/saas.update_subscription", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ plan_tier: selectedPlanTier.value }),
		});
		if (res.ok) {
			subscription.reload();
			showPlanModal.value = false;
		}
	} catch (err) {
		console.error("Error updating plan:", err);
	} finally {
		isUpdatingPlan.value = false;
	}
}
</script>
