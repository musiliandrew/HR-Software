<template>
	<div class="eliza-root">
		<!-- Header -->
		<header>
			<div class="w">
				<router-link class="logo" to="/">
					<i></i>eliza
				</router-link>

				<nav>
					<a href="#products">Platform</a>
					<a href="#solutions">Solutions</a>
					<a href="#stories">Customers</a>
					<a href="#support">Support</a>
					<a href="#insights">Resources</a>
				</nav>

				<div class="hr">
					<router-link to="/desk/hr-setup" class="o">HR Desk</router-link>
					<a href="http://127.0.0.1:8080" target="_blank" class="o">Employee PWA</a>
					<button class="btn" @click="openModal('Growth')">Get a demo</button>
				</div>
			</div>
		</header>

		<!-- Hero -->
		<div class="hero">
			<div class="w">
				<div style="padding-bottom: 64px">
					<small style="color: var(--mute); font-size: 12px">The connected construction & workforce platform</small>
					<h1 style="margin-top: 14px">Build with<br />confidence.</h1>
					<p>How modern contractors and companies manage payroll, HR, expenses, and field operations in one place.</p>
					
					<form class="form" @submit.prevent="submitHeroEmail">
						<input
							type="email"
							v-model="heroEmail"
							placeholder="Enter your work email"
							aria-label="Work email"
							required
						/>
						<button class="btn" type="submit">Get a demo</button>
					</form>
				</div>

				<div class="phone">
					<small>Welcome back to Eliza</small>
					<b>Crew overview</b>
					<div class="kp">
						<div>Hours today<strong>312</strong></div>
						<div>On site<strong>4</strong></div>
						<div>Crews<strong>253</strong></div>
					</div>
					<div class="bars">
						<span style="height: 40%"></span>
						<span style="height: 75%"></span>
						<span style="height: 55%"></span>
						<span style="height: 90%"></span>
						<span style="height: 35%"></span>
						<span style="height: 65%"></span>
					</div>
				</div>
			</div>

			<div class="w trust">
				<small>Trusted by 700+ contractors & growing enterprises</small>
				<div class="logos">
					<div>KNIGHT</div>
					<div>HARBOR</div>
					<div>WD</div>
					<div>GREEN</div>
					<div>ECC</div>
					<div>KL</div>
					<div>FH</div>
					<div>m</div>
					<div>TRUEBECK</div>
					<div>MECO</div>
				</div>
			</div>
		</div>

		<!-- Products Section -->
		<section id="products">
			<div class="w">
				<h2>Connect your people,<br />projects, and payments.</h2>
				
				<div class="tabs" role="tablist">
					<a href="#hcm" :class="{ active: activeTab === 'hcm' }" @click.prevent="scrollToTab('hcm')">HCM</a>
					<a href="#field" :class="{ active: activeTab === 'field' }" @click.prevent="scrollToTab('field')">Field Operations</a>
					<a href="#expense" :class="{ active: activeTab === 'expense' }" @click.prevent="scrollToTab('expense')">Expense Management</a>
				</div>

				<!-- Feat 1: HCM -->
				<div class="feat" id="hcm">
					<div>
						<span class="tag">HCM</span>
						<h3>Prioritize your people over paperwork.</h3>
						<p>Build a stronger workforce with less work. Eliza streamlines hiring, paying, developing and rewarding your team — so you can attract and retain top talent.</p>
						<router-link to="/desk/hr-setup" style="font-size: 14px; font-weight: 500">Explore HR Workspace &rarr;</router-link>
						<div class="tags">
							<span>HRIS</span>
							<span>Payroll</span>
							<span>Recruiting</span>
							<span>Benefits</span>
						</div>
					</div>
					<div class="pn m">
						<div class="card">
							<h4>Finalize your offer</h4>
							<div class="row">
								<span>Role</span>
								<span>Journeyman Electrician</span>
							</div>
							<div class="row">
								<span>Start date</span>
								<span>Tue, Apr 1</span>
							</div>
							<div class="row">
								<span>Pay rate</span>
								<span>$ 78.00 / hr</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Feat 2: Field Operations -->
				<div class="feat" id="field">
					<div>
						<span class="tag">Field Operations</span>
						<h3>Precision field reporting, made easy.</h3>
						<p>One system for time tracking, equipment, photos, and schedules. Ensure your field team spends less time juggling apps and more time focused on the job.</p>
						<router-link to="/roster" style="font-size: 14px; font-weight: 500">View Shift Roster &rarr;</router-link>
						<div class="tags">
							<span>Time Tracking</span>
							<span>Scheduling</span>
							<span>Production</span>
						</div>
					</div>
					<div class="pn t">
						<div class="card">
							<h4>Active timesheet</h4>
							<div class="timer">4:24:42</div>
							<div class="row">
								<span>Job</span>
								<span>SF-27 Hotel Building</span>
							</div>
							<div class="row">
								<span>Activity</span>
								<span>Pipe Fitting</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Feat 3: Expense Management -->
				<div class="feat" id="expense">
					<div>
						<span class="tag">Expense Management</span>
						<h3>Expense management for contractors.</h3>
						<p>Centralize expenses, per diems, and reimbursements alongside payroll and time tracking for seamless, stress-free job costing.</p>
						<a href="http://127.0.0.1:8080" target="_blank" style="font-size: 14px; font-weight: 500">Test on Mobile PWA &rarr;</a>
						<div class="tags">
							<span>Reimbursements</span>
							<span>Per Diems</span>
							<span>Corporate Cards</span>
						</div>
					</div>
					<div class="pn g">
						<div class="card">
							<h4>Reimbursements</h4>
							<div class="row">
								<span>Texaco</span>
								<span>$78.28 <span class="pill">Approved</span></span>
							</div>
							<div class="row">
								<span>Tolls</span>
								<span>$57.00 <span class="pill">Approved</span></span>
							</div>
							<div class="row">
								<span>Equipment Supply</span>
								<span>$109.47 <span class="pill" style="background: #fdf3e7; color: #8a6a43">Pending</span></span>
							</div>
						</div>
					</div>
				</div>

				<div class="cta" id="demo">
					<h4>Workforce management without the manual work.</h4>
					<button class="btn" @click="openModal('Growth')">Get a demo</button>
				</div>
			</div>
		</section>

		<!-- Customer Stories -->
		<section id="stories">
			<div class="w c">
				<h2>We've helped <em>700+</em> companies grow and manage their teams.</h2>
				<button class="btn o" style="margin-top: 8px" @click="openModal('Enterprise')">View all stories</button>

				<div class="story">
					<div>
						<div>
							<span class="meta">General Contractor</span>
							<h3 style="font-size: 32px; margin-top: 12px">How One of Florida's Biggest GCs Modernized Their Back Office with Eliza</h3>
						</div>
						<div>
							<a href="#" style="font-weight: 500; font-size: 14px" @click.prevent="openModal('Growth')">Read case study &rarr;</a>
							<div class="meta" style="margin-top: 20px">
								<span>200 employees</span>
								<span>Sage Intacct</span>
								<span>Procore</span>
								<span>Florida · North Carolina · Texas</span>
							</div>
						</div>
					</div>
					<div class="ph">
						<div class="play" aria-label="Play video" @click="openModal('Growth')">▶</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Platform Grid (Solutions) -->
		<section id="solutions" style="padding-top: 0">
			<div class="w">
				<h2>One platform, every piece in place.</h2>
				<div class="grid2">
					<div>
						<h3 style="font-size: 20px">Connected systems</h3>
						<p>Eliminate data silos and double entry by connecting HR, time tracking, project management, and accounting in one place.</p>
						<a href="#" @click.prevent="openModal('Growth')">Bring your systems together &rarr;</a>
					</div>
					<div>
						<h3 style="font-size: 20px">Compliance</h3>
						<p>Stay compliant without the headaches by automating certified payroll reporting, union fringes, and complex multi-state requirements.</p>
						<a href="#" @click.prevent="openModal('Enterprise')">Make compliance a breeze &rarr;</a>
					</div>
					<div>
						<h3 style="font-size: 20px">Job costing</h3>
						<p>Make better decisions by tracking equipment, materials, and fully-burdened labor costs to the cent — in real time.</p>
						<a href="#" @click.prevent="openModal('Growth')">Cost smarter &rarr;</a>
					</div>
					<div style="background: var(--bg); display: flex; flex-direction: column; justify-content: center; align-items: flex-start;">
						<h3 style="font-size: 20px">Multi-Tenant PostgreSQL</h3>
						<p>Built with enterprise database partition isolation on Neon Cloud for sub-second query execution.</p>
						<router-link to="/desk/hr-setup" style="font-weight: 500">Launch Management Desk &rarr;</router-link>
					</div>
				</div>
			</div>
		</section>

		<!-- Integrations -->
		<section style="padding-top: 0">
			<div class="w">
				<div class="int">
					<small style="text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600">Integrations</small>
					<h3>Eliza works with the tools you use.</h3>
					<p>Connect your workflows with integrations that actually work. Use our off-the-shelf integrations, or build a custom integration with our REST API.</p>
					<button class="btn" @click="openModal('Enterprise')">Explore all integrations</button>
					<div class="row2">
						<span>Acumatica</span>
						<span>Sage</span>
						<span>PREMIER</span>
						<span>ServiceTitan</span>
						<span>NetSuite</span>
						<span>Build</span>
					</div>
				</div>
			</div>
		</section>

		<!-- Support -->
		<section id="support" style="padding-top: 0">
			<div class="w sup">
				<small style="color: var(--mute); font-weight: 500; font-size: 13px">Support</small>
				<div>
					<h2 style="font-size: 32px">Get answers in minutes, not weeks.</h2>
					<div class="cards">
						<div>
							<h3 style="font-size: 18px">US-based support</h3>
							<p>Our US-based R&amp;D and support team provides hands-on onboarding and training, as well as fast responses via phone, email or in-app chat.</p>
							<div class="map"></div>
						</div>
						<div>
							<h3 style="font-size: 18px">White glove service</h3>
							<p>Eliza provides high-touch, premium implementation support to set up your team, configure your shifts, and ensure you're positioned for success.</p>
							<div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--line)">
								<strong style="display: block; font-size: 14px; margin-bottom: 6px">Employer-First B2B Model</strong>
								<p style="margin: 0; font-size: 13px">The company pays the predictable subscription. Free self-service access for all invited employees.</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Insights and Events -->
		<section id="insights" style="padding-top: 0">
			<div class="w">
				<h3 style="font-size: 28px; display: flex; justify-content: space-between; align-items: baseline">
					Insights and events
					<a href="#" style="font-size: 14px; color: var(--mute)">View all &rarr;</a>
				</h3>
				<div class="ins">
					<a href="#" @click.prevent="openModal('Growth')">
						<div class="im"></div>
						<h4>Three Signs It's Time for a New Construction Payroll Solution</h4>
						<span>Blog</span><span>Payroll</span>
					</a>
					<a href="#" @click.prevent="openModal('Growth')">
						<div class="im"></div>
						<h4>Why Generic Payroll Solutions Don't Cut It for Contractors</h4>
						<span>Blog</span><span>Compliance</span>
					</a>
					<a href="#" @click.prevent="openModal('Enterprise')">
						<div class="im"></div>
						<h4>Avoid Costly Work Authorization with E-Verify in Eliza</h4>
						<span>Events</span><span>Webinar</span>
					</a>
				</div>
			</div>
		</section>

		<!-- Final CTA -->
		<section class="final c">
			<div class="w">
				<h1 style="font-size: clamp(40px, 6vw, 64px)">Connect your HR, finance, and operations teams.</h1>
				<p style="color: var(--mute); max-width: 520px; margin: 20px auto 28px">
					Eliza is the missing piece that brings your payroll, payments and people together, so you can build with confidence.
				</p>
				<button class="btn" style="padding: 12px 28px; font-size: 16px" @click="openModal('Growth')">Get a demo</button>
			</div>
		</section>

		<!-- Footer -->
		<footer id="footer">
			<div class="w">
				<div class="fg">
					<router-link class="logo" to="/">
						<i></i>eliza
					</router-link>
					<div>
						<b>Products</b>
						<a href="#hcm">HCM</a>
						<a href="#field">Field Operations</a>
						<a href="#expense">Expense Management</a>
					</div>
					<div>
						<b>Features</b>
						<router-link to="/desk/hr-setup">HRIS &amp; Directory</router-link>
						<router-link to="/roster">Shift Rostering</router-link>
						<a href="http://127.0.0.1:8080" target="_blank">Mobile PWA</a>
						<a href="#hcm">Benefits &amp; Payroll</a>
					</div>
					<div>
						<b>Platform</b>
						<router-link to="/desk/hr-setup">HR Desk</router-link>
						<a href="#solutions">Connected Systems</a>
						<a href="#support">US Support</a>
					</div>
					<div>
						<b>Company</b>
						<a href="#stories">Customers</a>
						<a href="#insights">Insights</a>
						<a href="#" @click.prevent="openModal('Growth')">Get a demo</a>
					</div>
				</div>

				<div class="fb">
					<span>Get the latest from Eliza</span>
					<form class="form" style="margin: 0" @submit.prevent="submitNewsletter">
						<input type="email" v-model="newsletterEmail" placeholder="Work email" aria-label="Newsletter email" required />
						<button class="btn" type="submit">Subscribe</button>
					</form>
				</div>

				<div class="fb" style="border: 0; margin: 0; padding-top: 12px">
					<span>© 2026 Eliza Inc. All rights reserved.</span>
					<span>Privacy Policy &nbsp; Terms of Use</span>
				</div>
			</div>
		</footer>

		<!-- Company Registration & Demo Modal -->
		<div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
			<div class="modal-card">
				<button class="modal-close" @click="showModal = false">&times;</button>

				<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px">
					<span class="logo"><i></i>eliza</span>
					<span class="pill" style="margin-left: 8px">14-Day Free Trial</span>
				</div>

				<h3 style="font-size: 24px; margin-bottom: 6px">Get your Eliza Demo &amp; Workspace</h3>
				<p style="color: var(--mute); font-size: 13px; margin: 0 0 20px">
					The company lead is the subscriber. All employees you invite will access self-service tools for free.
				</p>

				<!-- Success Message -->
				<div v-if="successMessage" style="background: #e7f2ea; color: var(--green); border: 1px solid #c2e0cd; padding: 14px; border-radius: 6px; font-size: 13px; margin-bottom: 16px">
					<strong>{{ successMessage }}</strong>
					<p style="margin: 6px 0 0; font-size: 12px">Redirecting to your HR Setup Workspace in {{ redirectCountdown }}s...</p>
				</div>

				<!-- Error Message -->
				<div v-if="errorMessage" style="background: #fdf2f2; color: var(--maroon); border: 1px solid #f2cfcf; padding: 12px; border-radius: 6px; font-size: 13px; margin-bottom: 16px">
					{{ errorMessage }}
				</div>

				<!-- Form -->
				<form v-if="!successMessage" @submit.prevent="submitRegistration" style="display: flex; flex-direction: column; gap: 14px">
					<div>
						<label style="display: block; font-size: 12px; font-weight: 500; margin-bottom: 4px; color: var(--ink)">Company / Contractor Name</label>
						<input
							type="text"
							v-model="form.company_name"
							placeholder="e.g. Knight Construction Group"
							required
							class="modal-input"
						/>
					</div>

					<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px">
						<div>
							<label style="display: block; font-size: 12px; font-weight: 500; margin-bottom: 4px; color: var(--ink)">Lead Full Name</label>
							<input
								type="text"
								v-model="form.admin_name"
								placeholder="e.g. John Knight"
								required
								class="modal-input"
							/>
						</div>
						<div>
							<label style="display: block; font-size: 12px; font-weight: 500; margin-bottom: 4px; color: var(--ink)">Work Email</label>
							<input
								type="email"
								v-model="form.admin_email"
								placeholder="john@knightcg.com"
								required
								class="modal-input"
							/>
						</div>
					</div>

					<div>
						<label style="display: block; font-size: 12px; font-weight: 500; margin-bottom: 4px; color: var(--ink)">Password</label>
						<input
							type="password"
							v-model="form.password"
							placeholder="••••••••••••"
							required
							class="modal-input"
						/>
					</div>

					<div>
						<label style="display: block; font-size: 12px; font-weight: 500; margin-bottom: 4px; color: var(--ink)">Select Plan Tier</label>
						<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px">
							<button
								type="button"
								v-for="plan in ['Starter', 'Growth', 'Enterprise']"
								:key="plan"
								@click="form.plan_tier = plan"
								:class="['btn', form.plan_tier === plan ? '' : 'o']"
								style="padding: 8px; font-size: 12px; text-align: center"
							>
								{{ plan }}
							</button>
						</div>
					</div>

					<button
						type="submit"
						class="btn"
						:disabled="isSubmitting"
						style="width: 100%; padding: 12px; font-size: 14px; margin-top: 8px"
					>
						{{ isSubmitting ? 'Configuring Workspace...' : 'Create Company Workspace' }}
					</button>

					<p style="color: var(--mute); font-size: 11px; text-align: center; margin: 0">
						Includes instant access to the HR Setup Workspace, Month Roster, and Employee PWA.
					</p>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// State
const activeTab = ref("hcm");
const heroEmail = ref("");
const newsletterEmail = ref("");
const showModal = ref(false);
const isSubmitting = ref(false);
const errorMessage = ref("");
const successMessage = ref("");
const redirectCountdown = ref(3);

const form = ref({
	company_name: "",
	admin_name: "",
	admin_email: "",
	password: "",
	plan_tier: "Growth",
});

function scrollToTab(tabId: string) {
	activeTab.value = tabId;
	const el = document.getElementById(tabId);
	if (el) {
		el.scrollIntoView({ behavior: "smooth" });
	}
}

function openModal(plan: string = "Growth") {
	form.value.plan_tier = plan;
	if (heroEmail.value && !form.value.admin_email) {
		form.value.admin_email = heroEmail.value;
	}
	errorMessage.value = "";
	successMessage.value = "";
	showModal.value = true;
}

function submitHeroEmail() {
	openModal("Growth");
}

function submitNewsletter() {
	alert(`Thank you for subscribing with ${newsletterEmail.value}!`);
	newsletterEmail.value = "";
}

async function submitRegistration() {
	isSubmitting.value = true;
	errorMessage.value = "";
	successMessage.value = "";

	try {
		const response = await fetch("/api/method/saas.register_company", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-Tenant-Id": "NEW",
			},
			body: JSON.stringify(form.value),
		});

		const result = await response.json();

		if (response.ok && result.message && result.message.status === "success") {
			successMessage.value = `Welcome to Eliza! Registered ${form.value.company_name} on the ${form.value.plan_tier} Plan.`;

			let count = 3;
			redirectCountdown.value = count;
			const interval = setInterval(() => {
				count -= 1;
				redirectCountdown.value = count;
				if (count <= 0) {
					clearInterval(interval);
					showModal.value = false;
					router.push("/desk/hr-setup");
				}
			}, 1000);
		} else {
			errorMessage.value = result._error_message || result.exc || "Failed to register company. Please try again.";
		}
	} catch (err: any) {
		errorMessage.value = err.message || "Network error reaching Eliza backend server.";
	} finally {
		isSubmitting.value = false;
	}
}
</script>

<style scoped>
/* Eliza – The Connected Construction Platform Exact Design System */
.eliza-root {
	--bg: #f6f4ef;
	--surface: #fff;
	--ink: #1a1a1a;
	--mute: #6b6a66;
	--line: #dedbd3;
	--maroon: #5a1a1f;
	--green: #1f5a3a;
	--sand: #a8814f;
	--btn: #14110f;
	background: var(--bg);
	color: var(--ink);
	font: 400 16px/1.5 "Inter Tight", system-ui, -apple-system, sans-serif;
	min-height: 100vh;
	box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
	.eliza-root:not([data-theme="light"]) {
		--bg: #171513;
		--surface: #201d1a;
		--ink: #f1eee8;
		--mute: #a09c93;
		--line: #34302b;
		--btn: #f1eee8;
	}
}

* {
	box-sizing: border-box;
}

a {
	color: inherit;
	text-decoration: none;
}

a:focus-visible,
button:focus-visible,
input:focus-visible {
	outline: 2px solid var(--maroon);
	outline-offset: 2px;
}

.w {
	max-width: 1120px;
	margin: 0 auto;
	padding: 0 24px;
}

h1,
h2,
h3 {
	font-weight: 500;
	letter-spacing: -0.03em;
	line-height: 1.05;
	margin: 0;
	color: var(--ink);
}

h1 {
	font-size: clamp(44px, 7vw, 72px);
}
h2 {
	font-size: clamp(32px, 4.5vw, 48px);
}
h3 {
	font-size: clamp(28px, 3.4vw, 40px);
}

.btn {
	display: inline-block;
	background: var(--btn);
	color: var(--bg);
	border: 0;
	border-radius: 6px;
	padding: 10px 18px;
	font: 500 14px inherit;
	font-family: inherit;
	cursor: pointer;
	text-align: center;
	transition: opacity 0.15s ease;
}
.btn:hover {
	opacity: 0.9;
}
.btn.o {
	background: none;
	color: var(--ink);
	border: 1px solid var(--line);
}
.btn.o:hover {
	background: var(--surface);
}

header {
	position: sticky;
	top: 0;
	z-index: 50;
	background: var(--bg);
	border-bottom: 1px solid var(--line);
}

header .w {
	display: flex;
	align-items: center;
	height: 56px;
	gap: 32px;
}

.logo {
	font-weight: 600;
	font-size: 20px;
	letter-spacing: -0.04em;
	display: flex;
	gap: 8px;
	align-items: center;
	color: var(--ink);
}
.logo i {
	width: 18px;
	height: 18px;
	border-radius: 50% 50% 50% 0;
	background: var(--ink);
	display: inline-block;
}

nav {
	display: flex;
	gap: 28px;
	font-size: 14px;
	flex: 1;
	justify-content: center;
}
nav a {
	color: var(--mute);
	transition: color 0.15s ease;
}
nav a:hover {
	color: var(--ink);
}

.hr {
	display: flex;
	gap: 10px;
	align-items: center;
	font-size: 14px;
}
.hr .o {
	padding: 8px 12px;
	border: 1px solid var(--line);
	border-radius: 6px;
	font-size: 13px;
	color: var(--mute);
	background: var(--surface);
}
.hr .o:hover {
	color: var(--ink);
}

.hero {
	padding: 72px 0 0;
	border-bottom: 1px solid var(--line);
}
.hero .w {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 40px;
	align-items: end;
}
.hero p {
	color: var(--mute);
	max-width: 380px;
	margin: 20px 0 28px;
}

.form {
	display: flex;
	gap: 8px;
	max-width: 420px;
}
.form input {
	flex: 1;
	padding: 10px 12px;
	border: 1px solid var(--line);
	border-radius: 6px;
	background: var(--surface);
	color: var(--ink);
	font: inherit;
	font-size: 14px;
	min-width: 0;
}

.phone {
	justify-self: center;
	width: 280px;
	background: var(--surface);
	border: 1px solid var(--line);
	border-radius: 28px 28px 0 0;
	padding: 20px 18px 0;
	height: 360px;
	box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08);
}
.phone small {
	color: var(--mute);
	font-size: 12px;
}
.phone b {
	display: block;
	font-size: 15px;
	margin-bottom: 12px;
	font-weight: 500;
	color: var(--ink);
}

.kp {
	display: flex;
	gap: 8px;
	margin-bottom: 14px;
}
.kp div {
	flex: 1;
	border: 1px solid var(--line);
	border-radius: 8px;
	padding: 8px;
	font-size: 11px;
	color: var(--mute);
}
.kp strong {
	display: block;
	font-size: 20px;
	color: var(--ink);
	font-weight: 500;
}

.bars {
	display: flex;
	gap: 10px;
	align-items: flex-end;
	height: 110px;
	border-bottom: 1px solid var(--line);
	padding: 0 4px;
}
.bars span {
	flex: 1;
	background: var(--maroon);
	opacity: 0.85;
	border-radius: 3px 3px 0 0;
}
.bars span:nth-child(odd) {
	background: var(--sand);
}

.trust {
	padding: 32px 0 8px;
	text-align: center;
	font-size: 11px;
	color: var(--mute);
}
.logos {
	display: grid;
	grid-template-columns: repeat(5, 1fr);
	border-top: 1px solid var(--line);
	border-left: 1px solid var(--line);
	margin-top: 14px;
}
.logos div {
	border-right: 1px solid var(--line);
	border-bottom: 1px solid var(--line);
	height: 72px;
	display: grid;
	place-items: center;
	font-weight: 600;
	letter-spacing: 0.04em;
	color: var(--mute);
	font-size: 15px;
}

section {
	padding: 96px 0;
}

.tabs {
	display: flex;
	gap: 4px;
	margin: 40px 0 28px;
	padding: 4px;
	background: var(--surface);
	border: 1px solid var(--line);
	border-radius: 8px;
}
.tabs a {
	flex: 1;
	text-align: center;
	padding: 10px;
	font-size: 14px;
	border-radius: 6px;
	color: var(--mute);
	transition: all 0.15s ease;
}
.tabs a.active,
.tabs a:first-child:not(.inactive) {
	background: var(--bg);
	color: var(--ink);
}

.feat {
	display: grid;
	grid-template-columns: 1fr 1fr;
	border: 1px solid var(--line);
	background: var(--surface);
	margin-bottom: 28px;
	min-height: 420px;
}
.feat > div:first-child {
	padding: 48px;
	display: flex;
	flex-direction: column;
	justify-content: center;
	gap: 18px;
}
.feat p {
	color: var(--mute);
	max-width: 340px;
	margin: 0;
}
.feat .tags {
	font-size: 13px;
	color: var(--mute);
	display: flex;
	gap: 18px;
	margin-top: 20px;
}
.feat .tag {
	font-size: 13px;
	color: var(--mute);
	display: flex;
	gap: 8px;
	align-items: center;
}
.feat .tag:before {
	content: "";
	width: 8px;
	height: 8px;
	background: currentColor;
	border-radius: 2px;
}

.pn {
	display: grid;
	place-items: center;
	padding: 32px;
	overflow: hidden;
}
.pn.m {
	background: var(--maroon);
}
.pn.t {
	background: #8a6a43;
}
.pn.g {
	background: var(--green);
}

.card {
	background: #fff;
	color: #1a1a1a;
	border-radius: 12px;
	padding: 18px;
	width: 260px;
	font-size: 13px;
	box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}
.card h4 {
	margin: 0 0 12px;
	font-weight: 500;
	font-size: 15px;
}
.row {
	display: flex;
	justify-content: space-between;
	padding: 8px 0;
	border-top: 1px solid #eee;
}
.row span:first-child {
	color: #777;
}

.timer {
	font-size: 44px;
	font-weight: 500;
	letter-spacing: -0.03em;
	color: #1a1a1a;
}
.pill {
	font-size: 11px;
	background: #e7f2ea;
	color: var(--green);
	border-radius: 99px;
	padding: 2px 8px;
	display: inline-block;
}

.cta {
	border: 1px solid var(--line);
	background: var(--surface);
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 36px 40px;
	gap: 24px;
	flex-wrap: wrap;
}
.cta h4 {
	font-size: 22px;
	font-weight: 500;
	margin: 0;
	letter-spacing: -0.02em;
	max-width: 280px;
	line-height: 1.2;
}

.c {
	text-align: center;
}
.c h2 {
	max-width: 640px;
	margin: 0 auto 20px;
}
.c h2 em {
	font-style: normal;
	color: var(--maroon);
}

.story {
	display: grid;
	grid-template-columns: 1fr 1fr;
	background: var(--surface);
	border: 1px solid var(--line);
	margin-top: 48px;
	text-align: left;
}
.story > div:first-child {
	padding: 40px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	gap: 40px;
}
.story .ph {
	background: linear-gradient(135deg, #3b3a37, #8c8478);
	min-height: 300px;
	display: grid;
	place-items: center;
	color: #fff;
}
.play {
	width: 56px;
	height: 56px;
	border-radius: 50%;
	background: rgba(255, 255, 255, 0.9);
	display: grid;
	place-items: center;
	color: #222;
	cursor: pointer;
	box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.meta {
	font-size: 13px;
	color: var(--mute);
	display: flex;
	gap: 20px;
	flex-wrap: wrap;
}

.grid2 {
	display: grid;
	grid-template-columns: 1fr 1fr;
	border: 1px solid var(--line);
	background: var(--surface);
	margin-top: 40px;
}
.grid2 > div {
	padding: 32px;
	display: flex;
	flex-direction: column;
	gap: 12px;
	min-height: 260px;
}
.grid2 > div:nth-child(odd) {
	border-right: 1px solid var(--line);
}
.grid2 > div:nth-child(-n + 2) {
	border-bottom: 1px solid var(--line);
}
.grid2 p {
	color: var(--mute);
	margin: 0;
	font-size: 15px;
	max-width: 380px;
}
.grid2 a {
	font-size: 14px;
	margin-top: auto;
	font-weight: 500;
	color: var(--ink);
}

.int {
	background: var(--maroon);
	color: #f6efe6;
	border-radius: 4px;
	padding: 56px 40px 0;
	text-align: center;
}
.int h3 {
	font-size: 30px;
	margin: 8px 0 12px;
	color: #f6efe6;
}
.int p {
	max-width: 460px;
	margin: 0 auto 24px;
	color: #d8c8c0;
	font-size: 15px;
}
.int .btn {
	background: #fff;
	color: #1a1a1a;
}
.int .row2 {
	display: flex;
	justify-content: space-around;
	margin-top: 48px;
	padding: 32px 0;
	border-top: 1px solid #7a3a3f;
	font-size: 24px;
	font-weight: 600;
	gap: 16px;
	overflow-x: auto;
}

.sup {
	display: grid;
	grid-template-columns: 200px 1fr;
	gap: 32px;
}
.sup .cards {
	display: grid;
	grid-template-columns: 1fr 1fr;
	border: 1px solid var(--line);
	background: var(--surface);
	margin-top: 32px;
}
.sup .cards > div {
	padding: 28px;
	min-height: 280px;
}
.sup .cards > div:first-child {
	border-right: 1px solid var(--line);
}
.sup .cards p {
	color: var(--mute);
	font-size: 14px;
}

.map {
	height: 130px;
	background: radial-gradient(circle at 30% 50%, #9b86d6 0 30px, transparent 31px),
		radial-gradient(circle at 60% 40%, #cbbcf0 0 36px, transparent 37px),
		radial-gradient(circle at 75% 60%, #7a5fc2 0 22px, transparent 23px);
	margin-top: 12px;
	border-radius: 4px;
}

.ins {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	gap: 20px;
	margin-top: 32px;
}
.ins .im {
	height: 150px;
	background: #cfc9bc;
	margin-bottom: 12px;
	border-radius: 4px;
}
.ins a:nth-child(1) .im {
	background: #b9b3a6;
}
.ins h4 {
	margin: 0 0 8px;
	font-weight: 500;
	font-size: 16px;
	color: var(--ink);
}
.ins span {
	font-size: 12px;
	color: var(--mute);
	margin-right: 10px;
}

.final {
	background: linear-gradient(var(--bg), var(--surface));
}

footer {
	border-top: 1px solid var(--line);
	padding: 56px 0 24px;
	font-size: 14px;
}
.fg {
	display: grid;
	grid-template-columns: 1.2fr repeat(4, 1fr);
	gap: 24px;
}
.fg b {
	display: block;
	font-weight: 500;
	margin-bottom: 10px;
	color: var(--mute);
	font-size: 12px;
}
.fg a {
	display: block;
	padding: 3px 0;
	color: var(--ink);
}
.fb {
	display: flex;
	justify-content: space-between;
	gap: 16px;
	flex-wrap: wrap;
	border-top: 1px solid var(--line);
	margin-top: 48px;
	padding-top: 20px;
	color: var(--mute);
	font-size: 12px;
	align-items: center;
}

/* Modal styles tailored to the Eliza Design System */
.modal-overlay {
	position: fixed;
	inset: 0;
	z-index: 100;
	display: flex;
	align-items: center;
	justify-content: center;
	background: rgba(20, 17, 15, 0.6);
	backdrop-filter: blur(4px);
	padding: 16px;
}
.modal-card {
	background: var(--surface);
	color: var(--ink);
	border: 1px solid var(--line);
	border-radius: 12px;
	max-width: 500px;
	width: 100%;
	padding: 32px;
	position: relative;
	box-shadow: 0 24px 60px rgba(0, 0, 0, 0.2);
}
.modal-close {
	position: absolute;
	top: 16px;
	right: 16px;
	background: none;
	border: none;
	font-size: 24px;
	cursor: pointer;
	color: var(--mute);
}
.modal-close:hover {
	color: var(--ink);
}
.modal-input {
	width: 100%;
	padding: 10px 12px;
	border: 1px solid var(--line);
	border-radius: 6px;
	background: var(--bg);
	color: var(--ink);
	font: inherit;
	font-size: 14px;
	box-sizing: border-box;
}
.modal-input:focus {
	outline: 2px solid var(--maroon);
	background: var(--surface);
}

@media (max-width: 820px) {
	nav,
	.hr .o {
		display: none;
	}
	.hero .w,
	.feat,
	.story,
	.grid2,
	.sup,
	.sup .cards,
	.ins,
	.fg {
		grid-template-columns: 1fr;
	}
	.logos {
		grid-template-columns: repeat(2, 1fr);
	}
	.grid2 > div {
		border-right: 0 !important;
		border-bottom: 1px solid var(--line);
	}
	.sup .cards > div:first-child {
		border-right: 0;
	}
	.feat > div:first-child {
		padding: 32px 24px;
	}
	.tabs a {
		font-size: 12px;
	}
	header .w {
		justify-content: space-between;
	}
	.phone {
		height: 300px;
	}
}
</style>
