<template>
	<div class="min-h-screen bg-[#f6f4ef] text-[#1a1a1a] flex flex-col font-sans">
		<NavBar :user="user.data" />

		<!-- Workspace Container with Sidebar Navigation -->
		<div class="flex-1 flex max-w-[1400px] w-full mx-auto">
			<!-- Sidebar Navigation (Left Pane) -->
			<aside class="w-64 flex-shrink-0 border-r border-[#dedbd3] p-5 hidden md:flex flex-col justify-between">
				<div class="space-y-6">
					<!-- Company Switcher / Profile Box -->
					<div class="p-3.5 rounded-lg bg-white border border-[#dedbd3] shadow-xs">
						<div class="flex items-center space-x-2.5">
							<div class="h-9 w-9 rounded-md bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-sm">
								{{ (subscription.data?.company_name || 'E')[0] }}
							</div>
							<div class="min-w-0 flex-1">
								<h3 class="text-xs font-bold text-[#1a1a1a] truncate">
									{{ subscription.data?.company_name || 'Acme Corporation' }}
								</h3>
								<div class="flex items-center space-x-1 mt-0.5">
									<span class="inline-block w-1.5 h-1.5 rounded-full bg-[#1f5a3a]"></span>
									<span class="text-[10px] font-semibold text-[#1f5a3a]">
										{{ subscription.data?.plan_tier || 'Growth' }} Plan
									</span>
								</div>
							</div>
						</div>
					</div>

					<!-- Navigation Menu Groups -->
					<div class="space-y-4">
						<!-- Group 1: General -->
						<div>
							<span class="block px-3 text-[10px] font-bold text-[#6b6a66] uppercase tracking-wider mb-1.5">
								Workspace
							</span>
							<nav class="space-y-0.5 text-xs">
								<button
									@click="activeNav = 'overview'"
									:class="activeNav === 'overview' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
										</svg>
										<span>Dashboard Overview</span>
									</div>
								</button>

								<button
									@click="activeNav = 'employees'"
									:class="activeNav === 'employees' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
										</svg>
										<span>Employee Directory</span>
									</div>
									<span class="px-1.5 py-0.2 rounded text-[10px] font-semibold bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
										{{ employees.data?.length || 5 }}
									</span>
								</button>
							</nav>
						</div>

						<!-- Group 2: Operations -->
						<div>
							<span class="block px-3 text-[10px] font-bold text-[#6b6a66] uppercase tracking-wider mb-1.5">
								Operations
							</span>
							<nav class="space-y-0.5 text-xs">
								<router-link
									to="/roster"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60 transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
										</svg>
										<span>Shift Rostering</span>
									</div>
									<span class="text-[10px] text-[#6b6a66]">&rarr;</span>
								</router-link>

								<button
									@click="activeNav = 'attendance'"
									:class="activeNav === 'attendance' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
										</svg>
										<span>Live Attendance</span>
									</div>
									<span class="px-1.5 py-0.2 rounded-full text-[10px] font-semibold bg-[#e7f2ea] text-[#1f5a3a]">
										4 on site
									</span>
								</button>

								<button
									@click="activeNav = 'leaves'"
									:class="activeNav === 'leaves' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
										</svg>
										<span>Leave Management</span>
									</div>
									<span class="px-1.5 py-0.2 rounded-full text-[10px] font-semibold bg-[#fdf3e7] text-[#8a6a43]">
										1 pending
									</span>
								</button>

								<button
									@click="activeNav = 'departments'"
									:class="activeNav === 'departments' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
										</svg>
										<span>Departments</span>
									</div>
									<span class="px-1.5 py-0.2 rounded text-[10px] font-semibold bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
										{{ departmentsCount }}
									</span>
								</button>
							</nav>
						</div>

						<!-- Group 3: Account & Subscription -->
						<div>
							<span class="block px-3 text-[10px] font-bold text-[#6b6a66] uppercase tracking-wider mb-1.5">
								Subscription
							</span>
							<nav class="space-y-0.5 text-xs">
								<button
									@click="activeNav = 'subscription'"
									:class="activeNav === 'subscription' ? 'bg-white text-[#1a1a1a] font-bold shadow-xs border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-white/60'"
									class="w-full flex items-center justify-between px-3 py-2 rounded-md transition text-left"
								>
									<div class="flex items-center space-x-2.5">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
										</svg>
										<span>Plan &amp; Seats</span>
									</div>
									<span class="px-1.5 py-0.2 rounded text-[10px] font-semibold bg-[#e7f2ea] text-[#1f5a3a]">
										Active
									</span>
								</button>
							</nav>
						</div>
					</div>
				</div>

				<!-- Sidebar Footer -->
				<div class="pt-4 border-t border-[#dedbd3] space-y-2 text-xs">
					<a
						href="http://127.0.0.1:8080"
						target="_blank"
						class="flex items-center justify-between p-2 rounded-md bg-white border border-[#dedbd3] text-[#1a1a1a] hover:bg-[#f6f4ef] transition"
					>
						<span class="font-medium">Open Employee PWA</span>
						<span class="text-[11px] text-[#6b6a66]">&nearr;</span>
					</a>
					<router-link
						to="/"
						class="block text-center text-[11px] text-[#6b6a66] hover:text-[#1a1a1a] py-1 transition"
					>
						&larr; Back to Eliza Landing
					</router-link>
				</div>
			</aside>

			<!-- Main Workspace Content (Right Pane) -->
			<main class="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
				<!-- Workspace Sub-Header -->
				<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-[#dedbd3] pb-5">
					<div>
						<div class="flex items-center space-x-2">
							<h1 class="text-xl sm:text-2xl font-bold tracking-tight text-[#1a1a1a]">
								<span v-if="activeNav === 'overview'">Workspace Dashboard</span>
								<span v-else-if="activeNav === 'employees'">Employee Directory</span>
								<span v-else-if="activeNav === 'attendance'">Time &amp; Attendance</span>
								<span v-else-if="activeNav === 'leaves'">Leave &amp; Absence Policies</span>
								<span v-else-if="activeNav === 'departments'">Department Organization</span>
								<span v-else-if="activeNav === 'subscription'">Company Subscription &amp; Seats</span>
							</h1>
						</div>
						<p class="text-xs text-[#6b6a66] mt-0.5">
							{{ subscription.data?.company_name || 'Acme Corporation' }} &middot; {{ subscription.data?.plan_tier || 'Growth' }} Tier
						</p>
					</div>

					<!-- Header Action Buttons -->
					<div class="flex items-center space-x-2">
						<button
							@click="showAddModal = true"
							class="inline-flex items-center px-3.5 py-1.5 text-xs font-semibold rounded-md text-[#f6f4ef] bg-[#14110f] hover:opacity-90 shadow-xs transition"
						>
							+ Add Employee
						</button>
						<button
							@click="showPlanModal = true"
							class="inline-flex items-center px-3 py-1.5 text-xs font-medium rounded-md text-[#1a1a1a] bg-white border border-[#dedbd3] hover:bg-[#f6f4ef] transition"
						>
							Subscription
						</button>
					</div>
				</div>

				<!-- VIEW 1: OVERVIEW DASHBOARD -->
				<div v-if="activeNav === 'overview'" class="space-y-6">
					<!-- 4 KPI Cards -->
					<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
						<div class="bg-white p-4 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-[11px] font-bold text-[#6b6a66] uppercase tracking-wider">Total Workforce</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
									{{ subscription.data?.plan_tier || 'Growth' }}
								</span>
							</div>
							<div class="mt-2">
								<p class="text-2xl font-bold text-[#1a1a1a]">
									{{ employees.data?.length || 5 }} <span class="text-xs font-normal text-[#6b6a66]">/ {{ subscription.data?.seat_limit || 50 }} seats</span>
								</p>
								<div class="w-full bg-[#f6f4ef] h-1.5 rounded-full mt-2 overflow-hidden border border-[#dedbd3]">
									<div
										class="bg-[#14110f] h-full rounded-full"
										:style="{ width: `${Math.min(100, (((employees.data?.length || 5) / (subscription.data?.seat_limit || 50)) * 100))}%` }"
									></div>
								</div>
							</div>
							<p class="text-[11px] text-[#6b6a66] mt-2">
								{{ (subscription.data?.seat_limit || 50) - (employees.data?.length || 5) }} seats available
							</p>
						</div>

						<div class="bg-white p-4 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-[11px] font-bold text-[#6b6a66] uppercase tracking-wider">On Duty Today</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									● 80% On Site
								</span>
							</div>
							<div class="mt-2">
								<p class="text-2xl font-bold text-[#1f5a3a]">4 Active</p>
								<p class="text-[11px] text-[#6b6a66] mt-0.5">Mobile geo-verified check-ins</p>
							</div>
							<p class="text-[11px] text-[#6b6a66] mt-2">1 employee on scheduled leave</p>
						</div>

						<div class="bg-white p-4 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-[11px] font-bold text-[#6b6a66] uppercase tracking-wider">Pending Approvals</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#fdf3e7] text-[#8a6a43]">
									Review
								</span>
							</div>
							<div class="mt-2">
								<p class="text-2xl font-bold text-[#8a6a43]">2 to Review</p>
								<p class="text-[11px] text-[#6b6a66] mt-0.5">1 Annual leave &middot; 1 Expense claim</p>
							</div>
							<router-link to="/roster" class="text-[11px] text-[#1a1a1a] font-semibold mt-2 hover:underline">
								Review in shift roster &rarr;
							</router-link>
						</div>

						<div class="bg-white p-4 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-[11px] font-bold text-[#6b6a66] uppercase tracking-wider">Monthly Payroll</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									Completed
								</span>
							</div>
							<div class="mt-2">
								<p class="text-2xl font-bold text-[#1a1a1a]">$23,500</p>
								<p class="text-[11px] text-[#6b6a66] mt-0.5">Disbursal finalized for March 2026</p>
							</div>
							<p class="text-[11px] text-[#6b6a66] mt-2">Available on employee mobile PWA</p>
						</div>
					</div>

					<!-- Quick Directory Preview -->
					<div class="bg-white rounded-lg border border-[#dedbd3] shadow-xs overflow-hidden">
						<div class="px-5 py-3 border-b border-[#dedbd3] flex items-center justify-between">
							<h3 class="text-xs font-bold text-[#1a1a1a] uppercase tracking-wider">Recent Workforce Additions</h3>
							<button @click="activeNav = 'employees'" class="text-xs font-semibold text-[#1a1a1a] hover:underline">
								View All Directory &rarr;
							</button>
						</div>
						<div class="divide-y divide-[#dedbd3] text-xs">
							<div v-for="emp in (employees.data || []).slice(0, 3)" :key="emp.name" class="p-3.5 flex items-center justify-between hover:bg-[#f6f4ef]/50 transition">
								<div class="flex items-center space-x-3">
									<div class="h-8 w-8 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-xs">
										{{ emp.first_name ? emp.first_name[0] : 'E' }}
									</div>
									<div>
										<p class="font-bold text-[#1a1a1a]">{{ emp.employee_name }}</p>
										<p class="text-[11px] text-[#6b6a66]">{{ emp.designation || 'Staff' }} &middot; {{ emp.department || 'General' }}</p>
									</div>
								</div>
								<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									● Active
								</span>
							</div>
						</div>
					</div>
				</div>

				<!-- VIEW 2: FULL EMPLOYEE DIRECTORY -->
				<div v-else-if="activeNav === 'employees'" class="bg-white rounded-lg border border-[#dedbd3] shadow-xs flex flex-col overflow-hidden">
					<div class="px-5 py-3.5 border-b border-[#dedbd3] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
						<div class="flex items-center space-x-2">
							<h2 class="text-sm font-bold text-[#1a1a1a]">Team Members</h2>
							<span class="text-xs text-[#6b6a66] bg-[#f6f4ef] px-2 py-0.5 rounded border border-[#dedbd3]">
								{{ filteredEmployees.length }} Records
							</span>
						</div>

						<div class="relative w-full sm:w-64">
							<input
								type="text"
								v-model="searchQuery"
								placeholder="Filter by name, designation, dept..."
								class="w-full text-xs px-3 py-1.5 rounded border border-[#dedbd3] bg-[#f6f4ef] text-[#1a1a1a] placeholder-[#6b6a66] focus:bg-white focus:outline-none"
							/>
						</div>
					</div>

					<div class="overflow-x-auto">
						<table class="w-full text-left text-xs divide-y divide-[#dedbd3]">
							<thead class="bg-[#f6f4ef] text-[#6b6a66] uppercase font-bold text-[10px] tracking-wider">
								<tr>
									<th class="px-5 py-3">Member</th>
									<th class="px-5 py-3">Designation</th>
									<th class="px-5 py-3">Department</th>
									<th class="px-5 py-3 text-center">Status</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-[#dedbd3] bg-white text-[#1a1a1a]">
								<tr v-for="emp in filteredEmployees" :key="emp.name" class="hover:bg-[#f6f4ef]/60 transition">
									<td class="px-5 py-3 whitespace-nowrap">
										<div class="flex items-center space-x-2.5">
											<div class="h-7 w-7 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-[11px]">
												{{ emp.first_name ? emp.first_name[0] : (emp.employee_name ? emp.employee_name[0] : 'E') }}
											</div>
											<div>
												<div class="font-bold text-[#1a1a1a]">{{ emp.employee_name }}</div>
												<div class="text-[10px] text-[#6b6a66]">{{ emp.user_id || emp.name }}</div>
											</div>
										</div>
									</td>
									<td class="px-5 py-3 whitespace-nowrap text-[#6b6a66]">
										{{ emp.designation || "Staff" }}
									</td>
									<td class="px-5 py-3 whitespace-nowrap">
										<span class="inline-block px-2 py-0.5 rounded text-[10px] bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
											{{ emp.department || "General" }}
										</span>
									</td>
									<td class="px-5 py-3 whitespace-nowrap text-center">
										<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
											● {{ emp.status || "Active" }}
										</span>
									</td>
								</tr>
								<tr v-if="filteredEmployees.length === 0">
									<td colspan="4" class="px-5 py-8 text-center text-[#6b6a66]">
										No team members match "{{ searchQuery }}".
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>

				<!-- VIEW 3: LIVE ATTENDANCE -->
				<div v-else-if="activeNav === 'attendance'" class="space-y-4">
					<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs">
						<h3 class="text-sm font-bold text-[#1a1a1a] mb-1">Today's Geofenced Clock-ins</h3>
						<p class="text-xs text-[#6b6a66] mb-4">Real-time attendance logs submitted via Employee Mobile PWA.</p>
						<div class="space-y-2 text-xs">
							<div class="p-3 rounded-lg border border-[#dedbd3] bg-[#f6f4ef] flex items-center justify-between">
								<div class="flex items-center space-x-3">
									<span class="h-2 w-2 rounded-full bg-emerald-500"></span>
									<div>
										<p class="font-bold text-[#1a1a1a]">John Doe &middot; Senior Software Engineer</p>
										<p class="text-[10px] text-[#6b6a66]">HQ Office Geofence (40.7128, -74.0060)</p>
									</div>
								</div>
								<div class="text-right">
									<span class="font-mono font-bold text-[#1a1a1a]">08:58 AM</span>
									<span class="block text-[10px] font-bold text-[#1f5a3a]">On Time</span>
								</div>
							</div>

							<div class="p-3 rounded-lg border border-[#dedbd3] bg-[#f6f4ef] flex items-center justify-between">
								<div class="flex items-center space-x-3">
									<span class="h-2 w-2 rounded-full bg-emerald-500"></span>
									<div>
										<p class="font-bold text-[#1a1a1a]">Alice Smith &middot; Product Designer</p>
										<p class="text-[10px] text-[#6b6a66]">Remote Verified (IP 192.168.1.45)</p>
									</div>
								</div>
								<div class="text-right">
									<span class="font-mono font-bold text-[#1a1a1a]">09:02 AM</span>
									<span class="block text-[10px] font-bold text-[#1f5a3a]">On Time</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- VIEW 4: LEAVE POLICIES -->
				<div v-else-if="activeNav === 'leaves'" class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs space-y-4">
					<div>
						<h3 class="text-sm font-bold text-[#1a1a1a] mb-1">2026 Company Leave Categories</h3>
						<p class="text-xs text-[#6b6a66]">Configured time-off types available for employee self-service applications.</p>
					</div>
					<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
						<div v-for="lt in leaveTypes.data || defaultLeaveTypes" :key="lt" class="p-3.5 rounded-lg border border-[#dedbd3] bg-[#f6f4ef]">
							<h4 class="font-bold text-xs text-[#1a1a1a]">{{ lt }}</h4>
							<p class="text-[11px] text-[#6b6a66] mt-1">21 allocated days / year</p>
							<span class="inline-block mt-2 px-1.5 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">Active Policy</span>
						</div>
					</div>
				</div>

				<!-- VIEW 5: DEPARTMENTS -->
				<div v-else-if="activeNav === 'departments'" class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs space-y-4">
					<div>
						<h3 class="text-sm font-bold text-[#1a1a1a] mb-1">Organization Structure</h3>
						<p class="text-xs text-[#6b6a66]">Distribution of employees across functional business units.</p>
					</div>
					<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
						<div v-for="(count, dept) in departmentBreakdown" :key="dept" class="p-3.5 rounded-lg border border-[#dedbd3] bg-[#f6f4ef] flex items-center justify-between">
							<div>
								<p class="font-bold text-[#1a1a1a]">{{ dept }}</p>
								<p class="text-[10px] text-[#6b6a66]">{{ count }} team members</p>
							</div>
							<span class="px-2 py-0.5 rounded bg-white border border-[#dedbd3] text-xs font-bold text-[#1a1a1a]">
								{{ count }}
							</span>
						</div>
					</div>
				</div>

				<!-- VIEW 6: SUBSCRIPTION & BILLING -->
				<div v-else-if="activeNav === 'subscription'" class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs space-y-6">
					<div>
						<h3 class="text-sm font-bold text-[#1a1a1a] mb-1">Active Company Subscription</h3>
						<p class="text-xs text-[#6b6a66]">Employer-paid monthly subscription tier and seat allocations.</p>
					</div>

					<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
						<div class="p-4 rounded-lg border border-[#dedbd3] bg-[#f6f4ef]">
							<span class="text-[#6b6a66] uppercase text-[10px] font-bold tracking-wider">Plan Tier</span>
							<p class="text-xl font-bold text-[#1a1a1a] mt-1">{{ subscription.data?.plan_tier || 'Growth' }} Plan</p>
							<p class="text-[11px] text-[#1f5a3a] font-bold mt-1">● Active Auto-renew</p>
						</div>
						<div class="p-4 rounded-lg border border-[#dedbd3] bg-[#f6f4ef]">
							<span class="text-[#6b6a66] uppercase text-[10px] font-bold tracking-wider">Seat Usage</span>
							<p class="text-xl font-bold text-[#1a1a1a] mt-1">{{ employees.data?.length || 5 }} / {{ subscription.data?.seat_limit || 50 }}</p>
							<p class="text-[11px] text-[#6b6a66] mt-1">{{ (subscription.data?.seat_limit || 50) - (employees.data?.length || 5) }} available seats</p>
						</div>
						<div class="p-4 rounded-lg border border-[#dedbd3] bg-[#f6f4ef]">
							<span class="text-[#6b6a66] uppercase text-[10px] font-bold tracking-wider">Monthly Fee</span>
							<p class="text-xl font-bold text-[#1a1a1a] mt-1">${{ subscription.data?.monthly_price || 79 }}.00</p>
							<p class="text-[11px] text-[#6b6a66] mt-1">Free employee mobile app access</p>
						</div>
					</div>

					<div class="pt-2">
						<button
							@click="showPlanModal = true"
							class="px-4 py-2 rounded bg-[#14110f] text-[#f6f4ef] font-bold text-xs hover:opacity-90 transition"
						>
							Change / Upgrade Plan
						</button>
					</div>
				</div>
			</main>
		</div>

		<!-- Add Employee Modal -->
		<div v-if="showAddModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm" @click.self="showAddModal = false">
			<div class="bg-white border border-[#dedbd3] rounded-lg max-w-md w-full p-6 shadow-xl relative text-[#1a1a1a]">
				<button @click="showAddModal = false" class="absolute top-4 right-4 text-[#6b6a66] hover:text-[#1a1a1a] text-lg">&times;</button>
				<h3 class="text-base font-bold mb-1">Add Team Member</h3>
				<p class="text-xs text-[#6b6a66] mb-4">
					Employees receive free self-service access on mobile & web under your company plan.
				</p>

				<div v-if="addError" class="p-2.5 mb-3 rounded bg-red-50 border border-red-200 text-red-700 text-xs font-semibold">
					{{ addError }}
				</div>

				<form @submit.prevent="submitAddEmployee" class="space-y-3 text-xs">
					<div>
						<label class="block font-bold mb-1 text-[#6b6a66]">Full Legal Name</label>
						<input
							type="text"
							v-model="newEmp.employee_name"
							placeholder="e.g. Michael Scott"
							required
							class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
						/>
					</div>
					<div>
						<label class="block font-bold mb-1 text-[#6b6a66]">Work Email</label>
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
							<label class="block font-bold mb-1 text-[#6b6a66]">Department</label>
							<input
								type="text"
								v-model="newEmp.department"
								placeholder="Operations"
								required
								class="w-full px-3 py-2 rounded border border-[#dedbd3] bg-[#f6f4ef] focus:bg-white focus:outline-none"
							/>
						</div>
						<div>
							<label class="block font-bold mb-1 text-[#6b6a66]">Designation</label>
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
						class="w-full py-2.5 mt-2 rounded bg-[#14110f] text-[#f6f4ef] font-bold text-xs hover:opacity-90 transition disabled:opacity-50"
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
				<h3 class="text-base font-bold mb-1">Company Subscription Plan</h3>
				<p class="text-xs text-[#6b6a66] mb-4">
					The employer pays one flat monthly subscription. Select a tier to expand employee seats.
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
								<strong class="text-sm font-bold">{{ plan.name }}</strong>
								<span v-if="subscription.data?.plan_tier === plan.name" class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									Current Plan
								</span>
							</div>
							<p class="text-xs text-[#6b6a66] mt-0.5">{{ plan.description }}</p>
							<p class="text-xs font-bold text-[#1a1a1a] mt-1">{{ plan.seats }} Employee Seats</p>
						</div>
						<div class="text-right">
							<span class="text-base font-bold text-[#1a1a1a]">${{ plan.price }}</span>
							<span class="text-[11px] text-[#6b6a66]">/mo</span>
						</div>
					</div>
				</div>

				<button
					@click="submitPlanChange"
					:disabled="isUpdatingPlan || selectedPlanTier === subscription.data?.plan_tier"
					class="w-full py-2.5 mt-4 rounded bg-[#14110f] text-[#f6f4ef] font-bold text-xs hover:opacity-90 transition disabled:opacity-50"
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

const activeNav = ref("overview");
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

const departmentsCount = computed(() => {
	return Object.keys(departmentBreakdown.value).length;
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
