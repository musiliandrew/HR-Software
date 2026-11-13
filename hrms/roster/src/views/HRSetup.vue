<template>
	<div class="h-screen w-screen bg-[#f6f4ef] text-[#1a1a1a] flex overflow-hidden font-sans select-none">
		<!-- ============================================================ -->
		<!-- SIDEBAR SECTION 1: PRIMARY ICON RAIL (Leftmost Slender Bar) -->
		<!-- ============================================================ -->
		<aside class="w-16 flex-shrink-0 bg-white border-r border-[#dedbd3] flex flex-col items-center justify-between py-3 z-30 shadow-xs">
			<!-- Top: Brand Logo, Search & Notifications -->
			<div class="flex flex-col items-center space-y-4 w-full">
				<!-- Brand Logo Mark -->
				<router-link to="/" class="group flex items-center justify-center p-1.5 rounded-lg hover:bg-[#f6f4ef] transition" title="Eliza Home">
					<img src="/eliza-logo-dark.png" alt="Eliza" class="h-7 w-auto object-contain" />
				</router-link>

				<!-- Quick Search -->
				<button
					@click="showSearchModal = true"
					class="w-10 h-10 rounded-lg flex items-center justify-center text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-[#f6f4ef] transition"
					title="Quick Search (Ctrl + K)"
				>
					<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
					</svg>
				</button>

				<!-- Notifications Bell with Unread Badge -->
				<div class="relative">
					<button
						@click="showNotifications = !showNotifications"
						class="w-10 h-10 rounded-lg flex items-center justify-center text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-[#f6f4ef] transition"
						title="Notifications"
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
						</svg>
						<span v-if="unreadCount > 0" class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-[#5a1a1f] ring-2 ring-white"></span>
					</button>

					<!-- Notifications Popover Drawer -->
					<div
						v-if="showNotifications"
						class="absolute left-14 top-0 w-80 bg-white border border-[#dedbd3] rounded-lg shadow-xl p-4 z-50 text-xs"
					>
						<div class="flex items-center justify-between border-b border-[#dedbd3] pb-2 mb-3">
							<strong class="text-sm font-semibold text-[#1a1a1a]">Notifications</strong>
							<span class="text-[10px] text-[#6b6a66]">{{ notifications.length }} updates</span>
						</div>
						<div class="space-y-2 max-h-72 overflow-y-auto">
							<div
								v-for="n in notifications"
								:key="n.id"
								class="p-2.5 rounded bg-[#f6f4ef] hover:bg-[#eee8dc] transition"
							>
								<div class="flex items-center justify-between">
									<strong class="font-semibold text-[#1a1a1a]">{{ n.title }}</strong>
									<span class="text-[10px] text-[#6b6a66]">{{ n.time }}</span>
								</div>
								<p class="text-[#6b6a66] mt-0.5 text-[11px]">{{ n.message }}</p>
							</div>
						</div>
					</div>
				</div>

				<div class="w-8 h-px bg-[#dedbd3] my-1"></div>

				<!-- Navigation Modules (First Tab Rail) -->
				<div class="flex flex-col items-center space-y-1 w-full px-2">
					<button
						v-for="mod in modules"
						:key="mod.id"
						@click="selectModule(mod.id)"
						:class="activeModule === mod.id ? 'bg-[#14110f] text-[#f6f4ef] shadow-xs' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-[#f6f4ef]'"
						class="w-11 h-11 rounded-lg flex items-center justify-center transition relative group"
						:title="mod.name"
					>
						<!-- Custom SVG Icons for each module -->
						<svg v-if="mod.id === 'hr_setup'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
						</svg>

						<svg v-else-if="mod.id === 'shift_attendance'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
						</svg>

						<svg v-else-if="mod.id === 'leaves'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
						</svg>

						<svg v-else-if="mod.id === 'expenses'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
						</svg>

						<svg v-else-if="mod.id === 'payroll'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
						</svg>

						<svg v-else-if="mod.id === 'performance'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
						</svg>

						<svg v-else-if="mod.id === 'tenure'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
						</svg>

						<svg v-else-if="mod.id === 'recruitment'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
						</svg>

						<svg v-else-if="mod.id === 'tax_benefits'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l4-2 4 2 4-2 4 2z" />
						</svg>

						<!-- Active pill indicator on left edge -->
						<span
							v-if="activeModule === mod.id"
							class="absolute -left-2 top-2.5 bottom-2.5 w-1 bg-[#5a1a1f] rounded-r"
						></span>
					</button>
				</div>
			</div>

			<!-- Bottom: User Avatar / Workspace Profile -->
			<div class="flex flex-col items-center space-y-2 pt-2 border-t border-[#dedbd3] w-full">
				<div class="h-9 w-9 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-xs cursor-pointer shadow-xs" :title="user.data?.full_name || 'Administrator'">
					{{ (user.data?.full_name || 'A')[0] }}
				</div>
			</div>
		</aside>

		<!-- ============================================================ -->
		<!-- SIDEBAR SECTION 2: CONTEXTUAL DRAWER (Adjacent Navigation)  -->
		<!-- ============================================================ -->
		<aside class="w-60 flex-shrink-0 bg-white border-r border-[#dedbd3] flex flex-col justify-between p-4 z-20 shadow-xs">
			<div class="space-y-5">
				<!-- Header of 2nd Tab: Name of the Tab Open -->
				<div class="border-b border-[#dedbd3] pb-3.5">
					<div class="flex items-center space-x-2">
						<h2 class="text-base font-bold text-[#1a1a1a] tracking-tight">
							{{ currentModuleName }}
						</h2>
					</div>
					<p class="text-[11px] text-[#6b6a66] mt-0.5">
						{{ subscription.data?.company_name || 'Acme Corporation' }}
					</p>
				</div>

				<!-- Navigation Items for currently open Module -->
				<nav class="space-y-1 text-xs">
					<button
						v-for="item in currentSubNavItems"
						:key="item.id"
						@click="activeSubItem = item.id"
						:class="activeSubItem === item.id ? 'bg-[#f6f4ef] text-[#1a1a1a] font-bold border border-[#dedbd3]' : 'text-[#6b6a66] hover:text-[#1a1a1a] hover:bg-[#f6f4ef]/60'"
						class="w-full flex items-center justify-between px-3 py-2.5 rounded-md transition text-left"
					>
						<span class="truncate">{{ item.label }}</span>
						<span v-if="item.badge" class="px-1.5 py-0.2 rounded text-[10px] font-bold bg-white text-[#1a1a1a] border border-[#dedbd3]">
							{{ item.badge }}
						</span>
					</button>
				</nav>
			</div>

			<!-- Bottom Quick Switch & App Link -->
			<div class="pt-4 border-t border-[#dedbd3] space-y-2 text-xs">
				<a
					href="http://127.0.0.1:8080"
					target="_blank"
					class="flex items-center justify-between p-2 rounded bg-[#f6f4ef] hover:bg-[#eee8dc] text-[#1a1a1a] transition"
				>
					<span class="font-medium text-[11px]">Employee Mobile App</span>
					<span class="text-[10px] text-[#6b6a66]">&nearr;</span>
				</a>
				<router-link
					to="/"
					class="block text-center text-[11px] text-[#6b6a66] hover:text-[#1a1a1a] transition py-0.5"
				>
					&larr; Back to Eliza Home
				</router-link>
			</div>
		</aside>

		<!-- ============================================================ -->
		<!-- MAIN WORKSPACE CONTENT AREA                                  -->
		<!-- ============================================================ -->
		<main class="flex-1 flex flex-col min-w-0 overflow-y-auto bg-[#f6f4ef]">
			<!-- Top Breadcrumb & Action Bar -->
			<header class="h-14 bg-white border-b border-[#dedbd3] px-6 flex items-center justify-between flex-shrink-0">
				<div class="flex items-center space-x-2 text-xs">
					<router-link to="/" class="font-semibold text-sm text-[#1a1a1a] hover:opacity-80 transition">
						eliza
					</router-link>
					<span class="text-[#6b6a66]">/</span>
					<span class="font-medium text-[#1a1a1a]">{{ currentModuleName }}</span>
					<span class="text-[#6b6a66]">/</span>
					<span class="font-bold text-[#14110f]">{{ currentSubItemLabel }}</span>
				</div>

				<div class="flex items-center space-x-2.5">
					<button
						@click="showAddModal = true"
						class="inline-flex items-center px-3.5 py-1.5 text-xs font-semibold rounded-md text-[#f6f4ef] bg-[#14110f] hover:opacity-90 shadow-xs transition"
					>
						+ Add Employee
					</button>
					<button
						@click="showPlanModal = true"
						class="inline-flex items-center px-3 py-1.5 text-xs font-medium rounded-md text-[#1a1a1a] bg-[#f6f4ef] border border-[#dedbd3] hover:bg-white transition"
					>
						{{ subscription.data?.plan_tier || 'Growth' }} Plan
					</button>
				</div>
			</header>

			<!-- Scrollable Page Content -->
			<div class="p-6 sm:p-8 space-y-6 flex-1">
				<!-- SUB-PAGE 1: HOME (Workspace Setup & Quick Operations) -->
				<div v-if="activeSubItem === 'home'" class="space-y-6">
					<!-- Welcome Hero Box -->
					<div class="bg-white rounded-lg border border-[#dedbd3] p-6 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
						<div>
							<div class="flex items-center space-x-2">
								<h2 class="text-xl font-bold text-[#1a1a1a]">
									Welcome to {{ subscription.data?.company_name || 'Acme Corporation' }}
								</h2>
								<span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a] border border-[#c2e0cd]">
									Live &middot; {{ subscription.data?.plan_tier || 'Growth' }} Tier
								</span>
							</div>
							<p class="text-xs text-[#6b6a66] mt-1 max-w-xl leading-relaxed">
								Your multi-tenant HR operating workspace is ready. Manage workforce records, verify mobile check-in geofences, approve leave applications, and run monthly payroll.
							</p>
						</div>

						<div class="flex items-center space-x-2 flex-shrink-0">
							<button
								@click="activeSubItem = 'dashboard'"
								class="px-3.5 py-2 rounded-md bg-[#14110f] text-[#f6f4ef] font-semibold text-xs hover:opacity-90 transition"
							>
								View Dashboard
							</button>
							<button
								@click="activeSubItem = 'masters'"
								class="px-3.5 py-2 rounded-md bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3] font-semibold text-xs hover:bg-white transition"
							>
								Manage Directory
							</button>
						</div>
					</div>

					<!-- Onboarding Progress Tracker -->
					<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs">
						<div class="flex items-center justify-between mb-3">
							<h3 class="text-xs font-bold text-[#1a1a1a] uppercase tracking-wider">Company Setup Progress</h3>
							<span class="text-xs font-bold text-[#1f5a3a]">75% Complete</span>
						</div>
						<div class="w-full bg-[#f6f4ef] h-2 rounded-full overflow-hidden border border-[#dedbd3] mb-4">
							<div class="bg-[#1f5a3a] h-full rounded-full" style="width: 75%"></div>
						</div>
						<div class="grid grid-cols-1 sm:grid-cols-4 gap-3 text-xs">
							<div class="p-3 rounded border border-[#dedbd3] bg-[#f6f4ef] flex items-center space-x-2">
								<span class="text-[#1f5a3a] font-bold">✓</span>
								<div>
									<p class="font-bold text-[#1a1a1a]">Company Registered</p>
									<p class="text-[10px] text-[#6b6a66]">{{ subscription.data?.company_name }}</p>
								</div>
							</div>
							<div class="p-3 rounded border border-[#dedbd3] bg-[#f6f4ef] flex items-center space-x-2">
								<span class="text-[#1f5a3a] font-bold">✓</span>
								<div>
									<p class="font-bold text-[#1a1a1a]">Workforce Seeded</p>
									<p class="text-[10px] text-[#6b6a66]">{{ employees.data?.length || 5 }} Team members</p>
								</div>
							</div>
							<div class="p-3 rounded border border-[#dedbd3] bg-[#f6f4ef] flex items-center space-x-2">
								<span class="text-[#1f5a3a] font-bold">✓</span>
								<div>
									<p class="font-bold text-[#1a1a1a]">Shifts Configured</p>
									<p class="text-[10px] text-[#6b6a66]">Morning & General</p>
								</div>
							</div>
							<div class="p-3 rounded border border-[#dedbd3] bg-white flex items-center space-x-2">
								<span class="text-[#bd710d] font-bold">●</span>
								<div>
									<p class="font-bold text-[#1a1a1a]">Employee PWA Invites</p>
									<p class="text-[10px] text-[#6b6a66]">Mobile check-in active</p>
								</div>
							</div>
						</div>
					</div>

					<!-- Quick Stats & Recent Updates -->
					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs">
							<h3 class="text-xs font-bold text-[#1a1a1a] uppercase tracking-wider mb-3">Quick Navigation</h3>
							<div class="space-y-2 text-xs">
								<button @click="activeSubItem = 'org_chart'" class="w-full p-2.5 rounded bg-[#f6f4ef] hover:bg-[#eee8dc] text-left flex items-center justify-between transition">
									<span class="font-semibold text-[#1a1a1a]">View Organizational Hierarchy Chart</span>
									<span class="text-[#6b6a66]">&rarr;</span>
								</button>
								<router-link to="/roster" class="w-full p-2.5 rounded bg-[#f6f4ef] hover:bg-[#eee8dc] text-left flex items-center justify-between transition">
									<span class="font-semibold text-[#1a1a1a]">Open Shift Rostering Calendar</span>
									<span class="text-[#6b6a66]">&rarr;</span>
								</router-link>
								<button @click="showPlanModal = true" class="w-full p-2.5 rounded bg-[#f6f4ef] hover:bg-[#eee8dc] text-left flex items-center justify-between transition">
									<span class="font-semibold text-[#1a1a1a]">Upgrade Company Subscription Tier</span>
									<span class="text-[#6b6a66]">&rarr;</span>
								</button>
							</div>
						</div>

						<div class="bg-white rounded-lg border border-[#dedbd3] p-5 shadow-xs">
							<h3 class="text-xs font-bold text-[#1a1a1a] uppercase tracking-wider mb-3">Department Summary</h3>
							<div class="space-y-2 text-xs">
								<div v-for="(count, dept) in departmentBreakdown" :key="dept" class="flex justify-between items-center p-2 rounded bg-[#f6f4ef]">
									<span class="font-medium text-[#1a1a1a]">{{ dept }}</span>
									<span class="font-bold text-[#6b6a66]">{{ count }} {{ count === 1 ? 'member' : 'members' }}</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- SUB-PAGE 2: DASHBOARD (4 HR KPI Metric Cards & Analytics) -->
				<div v-else-if="activeSubItem === 'dashboard'" class="space-y-6">
					<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
						<!-- Card 1: Total Workforce -->
						<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-xs font-bold text-[#6b6a66] uppercase tracking-wider">Total Workforce</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#f6f4ef] text-[#1a1a1a] border border-[#dedbd3]">
									{{ subscription.data?.plan_tier || 'Growth' }}
								</span>
							</div>
							<div class="mt-3">
								<p class="text-3xl font-bold text-[#1a1a1a]">
									{{ employees.data?.length || 5 }} <span class="text-xs font-normal text-[#6b6a66]">/ {{ subscription.data?.seat_limit || 50 }} seats</span>
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
						<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-xs font-bold text-[#6b6a66] uppercase tracking-wider">On Duty Today</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									● 80% On Site
								</span>
							</div>
							<div class="mt-3">
								<p class="text-3xl font-bold text-[#1f5a3a]">4 Active</p>
								<p class="text-xs text-[#6b6a66] mt-1">Geo-verified mobile clock-ins</p>
							</div>
							<p class="text-xs text-[#6b6a66] mt-3">1 staff scheduled off-shift</p>
						</div>

						<!-- Card 3: Pending Approvals -->
						<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-xs font-bold text-[#6b6a66] uppercase tracking-wider">Pending Requests</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#fdf3e7] text-[#8a6a43]">
									Review
								</span>
							</div>
							<div class="mt-3">
								<p class="text-3xl font-bold text-[#8a6a43]">2 to Review</p>
								<p class="text-xs text-[#6b6a66] mt-1">1 Annual leave &middot; 1 Expense claim</p>
							</div>
							<router-link to="/roster" class="text-xs text-[#1a1a1a] font-semibold mt-3 hover:underline">
								Review in shift roster &rarr;
							</router-link>
						</div>

						<!-- Card 4: Monthly Payroll Cycle -->
						<div class="bg-white p-5 rounded-lg border border-[#dedbd3] shadow-xs flex flex-col justify-between">
							<div class="flex items-center justify-between">
								<span class="text-xs font-bold text-[#6b6a66] uppercase tracking-wider">Monthly Payroll</span>
								<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
									March 2026
								</span>
							</div>
							<div class="mt-3">
								<p class="text-3xl font-bold text-[#1a1a1a]">$23,500</p>
								<p class="text-xs text-[#6b6a66] mt-1">Base gross & deductions finalized</p>
							</div>
							<p class="text-xs text-[#6b6a66] mt-3">Available on employee mobile PWA</p>
						</div>
					</div>
				</div>

				<!-- SUB-PAGE 3: ORGANIZATIONAL CHART (Visual Hierarchy Tree) -->
				<div v-else-if="activeSubItem === 'org_chart'" class="bg-white rounded-lg border border-[#dedbd3] p-6 shadow-xs space-y-6">
					<div>
						<h3 class="text-base font-bold text-[#1a1a1a]">Company Hierarchy & Organizational Chart</h3>
						<p class="text-xs text-[#6b6a66] mt-0.5">Visual reporting structure across leadership, departments, and staff.</p>
					</div>

					<!-- Visual Org Tree -->
					<div class="p-6 bg-[#f6f4ef] rounded-lg border border-[#dedbd3] flex flex-col items-center space-y-6 overflow-x-auto">
						<!-- Level 1: Company Lead / Director -->
						<div class="p-4 bg-white rounded-lg border-2 border-[#14110f] shadow-sm text-center w-64">
							<div class="h-10 w-10 mx-auto rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-sm mb-2">
								{{ (user.data?.full_name || 'A')[0] }}
							</div>
							<h4 class="font-bold text-sm text-[#1a1a1a]">{{ user.data?.full_name || 'Administrator' }}</h4>
							<p class="text-xs text-[#6b6a66] font-medium">Company Owner &middot; HR Director</p>
							<span class="inline-block mt-2 px-2 py-0.5 rounded text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">Executive Level</span>
						</div>

						<div class="w-0.5 h-6 bg-[#dedbd3]"></div>

						<!-- Level 2: Departments Tier -->
						<div class="grid grid-cols-1 sm:grid-cols-4 gap-4 w-full max-w-4xl">
							<div v-for="(count, dept) in departmentBreakdown" :key="dept" class="p-3.5 bg-white rounded-lg border border-[#dedbd3] text-center shadow-xs">
								<h5 class="font-bold text-xs text-[#1a1a1a]">{{ dept }}</h5>
								<p class="text-[11px] text-[#6b6a66] mt-0.5">{{ count }} Staff</p>
								<div class="mt-2 pt-2 border-t border-[#dedbd3] flex justify-center -space-x-1.5">
									<div v-for="i in Math.min(3, count)" :key="i" class="w-5 h-5 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center text-[9px] font-bold ring-1 ring-white">
										{{ dept[0] }}
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- SUB-PAGE 4: MASTERS (Employee Directory & Department Tables) -->
				<div v-else-if="activeSubItem === 'masters'" class="bg-white rounded-lg border border-[#dedbd3] shadow-xs flex flex-col overflow-hidden">
					<div class="px-6 py-4 border-b border-[#dedbd3] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
						<div class="flex items-center space-x-2">
							<h2 class="text-sm font-bold text-[#1a1a1a]">Employee Directory Master</h2>
							<span class="text-xs text-[#6b6a66] bg-[#f6f4ef] px-2 py-0.5 rounded border border-[#dedbd3]">
								{{ filteredEmployees.length }} Records
							</span>
						</div>

						<div class="flex items-center space-x-2">
							<input
								type="text"
								v-model="searchQuery"
								placeholder="Search employee, role, dept..."
								class="text-xs px-3 py-1.5 rounded border border-[#dedbd3] bg-[#f6f4ef] text-[#1a1a1a] focus:bg-white focus:outline-none w-56"
							/>
							<button
								@click="showAddModal = true"
								class="px-3 py-1.5 text-xs font-semibold rounded bg-[#14110f] text-[#f6f4ef] hover:opacity-90 transition"
							>
								+ New
							</button>
						</div>
					</div>

					<div class="overflow-x-auto">
						<table class="w-full text-left text-xs divide-y divide-[#dedbd3]">
							<thead class="bg-[#f6f4ef] text-[#6b6a66] uppercase font-bold text-[10px] tracking-wider">
								<tr>
									<th class="px-6 py-3">Member</th>
									<th class="px-6 py-3">Designation</th>
									<th class="px-6 py-3">Department</th>
									<th class="px-6 py-3 text-center">Status</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-[#dedbd3] bg-white text-[#1a1a1a]">
								<tr v-for="emp in filteredEmployees" :key="emp.name" class="hover:bg-[#f6f4ef]/60 transition">
									<td class="px-6 py-3.5 whitespace-nowrap">
										<div class="flex items-center space-x-3">
											<div class="h-8 w-8 rounded-full bg-[#14110f] text-[#f6f4ef] flex items-center justify-center font-bold text-xs">
												{{ emp.first_name ? emp.first_name[0] : (emp.employee_name ? emp.employee_name[0] : 'E') }}
											</div>
											<div>
												<div class="font-bold text-[#1a1a1a]">{{ emp.employee_name }}</div>
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
										<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-[#e7f2ea] text-[#1f5a3a]">
											● {{ emp.status || "Active" }}
										</span>
									</td>
								</tr>
								<tr v-if="filteredEmployees.length === 0">
									<td colspan="4" class="px-6 py-8 text-center text-[#6b6a66]">
										No members match "{{ searchQuery }}".
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>

				<!-- SUB-PAGE 5: SETTINGS (Company Profile & Subscription Seats) -->
				<div v-else-if="activeSubItem === 'settings'" class="bg-white rounded-lg border border-[#dedbd3] p-6 shadow-xs space-y-6">
					<div>
						<h3 class="text-base font-bold text-[#1a1a1a]">Company &amp; Workspace Settings</h3>
						<p class="text-xs text-[#6b6a66] mt-0.5">Manage subscription tier, employee seat capacity, and organization profile.</p>
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
			</div>
		</main>

		<!-- ============================================================ -->
		<!-- MODALS: ADD EMPLOYEE, CHANGE PLAN, SEARCH                    -->
		<!-- ============================================================ -->
		<!-- Quick Search Modal (Ctrl + K) -->
		<div v-if="showSearchModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm" @click.self="showSearchModal = false">
			<div class="bg-white border border-[#dedbd3] rounded-lg max-w-lg w-full p-5 shadow-2xl relative text-[#1a1a1a]">
				<div class="flex items-center border-b border-[#dedbd3] pb-3">
					<svg class="w-5 h-5 text-[#6b6a66] mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
					</svg>
					<input
						type="text"
						v-model="spotlightQuery"
						placeholder="Search any employee, shift, leave, or setting..."
						class="w-full text-sm outline-none bg-transparent placeholder-[#6b6a66]"
						autofocus
					/>
				</div>
				<div class="mt-3 space-y-1 text-xs max-h-60 overflow-y-auto">
					<div
						v-for="emp in filteredSpotlight"
						:key="emp.name"
						@click="activeSubItem = 'masters'; showSearchModal = false"
						class="p-2 rounded hover:bg-[#f6f4ef] flex items-center justify-between cursor-pointer"
					>
						<div>
							<strong class="text-[#1a1a1a]">{{ emp.employee_name }}</strong>
							<span class="text-[#6b6a66] ml-2">({{ emp.designation }} &middot; {{ emp.department }})</span>
						</div>
						<span class="text-[10px] text-[#6b6a66]">&rarr;</span>
					</div>
				</div>
			</div>
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

// Modules for First Sidebar Rail
const modules = [
	{ id: "hr_setup", name: "HR Setup" },
	{ id: "shift_attendance", name: "Shift and Attendance" },
	{ id: "leaves", name: "Leaves" },
	{ id: "expenses", name: "Expenses" },
	{ id: "payroll", name: "Payroll" },
	{ id: "performance", name: "Performance" },
	{ id: "tenure", name: "Tenure" },
	{ id: "recruitment", name: "Recruitment" },
	{ id: "tax_benefits", name: "Tax and Benefits" },
];

const activeModule = ref("hr_setup");
const activeSubItem = ref("home");

// UI state
const searchQuery = ref("");
const spotlightQuery = ref("");
const showSearchModal = ref(false);
const showNotifications = ref(false);
const showAddModal = ref(false);
const showPlanModal = ref(false);
const isSubmittingEmp = ref(false);
const isUpdatingPlan = ref(false);
const addError = ref("");
const selectedPlanTier = ref("Growth");
const unreadCount = ref(2);

const notifications = ref([
	{ id: 1, title: "Leave Request Submitted", message: "John Doe submitted an Annual Leave application for 3 days.", time: "10m ago" },
	{ id: 2, title: "Expense Claim Pending", message: "Alice Smith submitted a claim for $109.47.", time: "1h ago" },
	{ id: 3, title: "Payroll Disbursal Ready", message: "March 2026 payroll cycle finalized.", time: "Yesterday" },
]);

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

// Sub-navigation mappings for the 2nd Sidebar Tab
const subNavMap: Record<string, { label: string; items: { id: string; label: string; badge?: string }[] }> = {
	hr_setup: {
		label: "HR Setup",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Dashboard" },
			{ id: "org_chart", label: "Organizational chart" },
			{ id: "masters", label: "Masters" },
			{ id: "settings", label: "Settings" },
		],
	},
	shift_attendance: {
		label: "Shift and Attendance",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Attendance Summary", badge: "4 on site" },
			{ id: "masters", label: "Shift Types" },
			{ id: "settings", label: "Roster Settings" },
		],
	},
	leaves: {
		label: "Leaves",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Applications", badge: "1 pending" },
			{ id: "masters", label: "Leave Allocations" },
			{ id: "settings", label: "Holiday Calendar" },
		],
	},
	expenses: {
		label: "Expenses",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Claims & Receipts", badge: "1 to review" },
			{ id: "masters", label: "Expense Claim Types" },
			{ id: "settings", label: "Approval Policies" },
		],
	},
	payroll: {
		label: "Payroll",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Salary Slips", badge: "March 2026" },
			{ id: "masters", label: "Salary Structures" },
			{ id: "settings", label: "Tax & Bank Slabs" },
		],
	},
	performance: {
		label: "Performance",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Appraisal Cycles" },
			{ id: "masters", label: "Goals & KPIs" },
			{ id: "settings", label: "Evaluation Criteria" },
		],
	},
	tenure: {
		label: "Tenure",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Lifecycle Overview" },
			{ id: "masters", label: "Promotions & Transfers" },
			{ id: "settings", label: "Separation Checklists" },
		],
	},
	recruitment: {
		label: "Recruitment",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Job Openings" },
			{ id: "masters", label: "Candidate Pipeline" },
			{ id: "settings", label: "Interview Templates" },
		],
	},
	tax_benefits: {
		label: "Tax and Benefits",
		items: [
			{ id: "home", label: "Home" },
			{ id: "dashboard", label: "Benefit Plans" },
			{ id: "masters", label: "Tax Declarations" },
			{ id: "settings", label: "Deduction Rules" },
		],
	},
};

// Resources
const user = createResource({
	url: "hrms.api.get_current_user_info",
	auto: true,
});

const employees = createResource({
	url: "hrms.api.get_all_employees",
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
const currentModuleName = computed(() => {
	return subNavMap[activeModule.value]?.label || "HR Setup";
});

const currentSubNavItems = computed(() => {
	return subNavMap[activeModule.value]?.items || subNavMap.hr_setup.items;
});

const currentSubItemLabel = computed(() => {
	const match = currentSubNavItems.value.find((i) => i.id === activeSubItem.value);
	return match ? match.label : "Home";
});

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

const filteredSpotlight = computed(() => {
	const list = employees.data || [];
	if (!spotlightQuery.value.trim()) return list;
	const q = spotlightQuery.value.toLowerCase();
	return list.filter((emp: any) =>
		(emp.employee_name && emp.employee_name.toLowerCase().includes(q)) ||
		(emp.designation && emp.designation.toLowerCase().includes(q)) ||
		(emp.department && emp.department.toLowerCase().includes(q))
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

// Methods
function selectModule(modId: string) {
	activeModule.value = modId;
	// When switching modules, reset to 'home'
	activeSubItem.value = "home";
}

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
