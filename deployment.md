# Deployment Instructions

Since this is a static website (HTML, CSS, JS), you can deploy it for free on platforms like **Netlify** or **GitHub Pages**.

## Option 1: Netlify (Recommended - Easiest)
1.  Go to [Netlify Drop](https://app.netlify.com/drop).
2.  Drag and drop the `portfolio` folder (located at `c:/Users/91996/Desktop/portfolio`) into the upload area.
3.  Netlify will automatically deploy your site and give you a live URL (e.g., `random-name.netlify.app`).
4.  You can change the site name in "Site settings" -> "Change site name".

## Option 2: GitHub Pages
1.  Create a new repository on GitHub (e.g., `my-portfolio`).
2.  Push your code to this repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/my-portfolio.git
    git push -u origin main
    ```
3.  Go to the repository **Settings** -> **Pages**.
4.  Under **Source**, select `main` branch and click **Save**.
5.  Your site will be live at `https://YOUR_USERNAME.github.io/my-portfolio`.

### Setting up a Custom Domain (GitHub Pages)
If you have bought a domain (e.g., `karthik-portfolio.com`) from a provider like GoDaddy or Namecheap:

1.  **Configure DNS (at your Domain Provider):**
    *   Go to your domain provider's DNS settings.
    *   Add **four "A" records** pointing to GitHub's IP addresses:
        *   `185.199.108.153`
        *   `185.199.109.153`
        *   `185.199.110.153`
        *   `185.199.111.153`
    *   Add a **"CNAME" record** for `www` pointing to your GitHub username:
        *   Host: `www`
        *   Value: `YOUR_USERNAME.github.io`

2.  **Configure GitHub:**
    *   Go to your repository **Settings** -> **Pages**.
    *   In the **Custom domain** field, enter your domain (e.g., `karthik-portfolio.com`).
    *   Click **Save**.
    *   GitHub will create a file named `CNAME` in your repository.
    *   Check the **Enforce HTTPS** box (it might take a few minutes to become available).

## Option 3: Vercel
1.  Install Vercel CLI: `npm i -g vercel`
2.  Run `vercel` in the terminal within the `portfolio` folder.
3.  Follow the prompts (mostly just press Enter).
