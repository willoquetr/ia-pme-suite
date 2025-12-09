# Copyright Notice

## IA PME Suite

**Copyright © 2025 Rudy Willoquet (IA PME)**  
All Rights Reserved.

### Project Information
- **Name**: IA PME Suite
- **Version**: 1.0.0
- **Release Date**: December 2025
- **Homepage**: https://willoquetr.github.io/ia-pme-suite/
- **Repository**: https://github.com/willoquetr/ia-pme-suite

### Author
**Rudy Willoquet**  
Email: willoquetr@gmail.com  
Location: Bretagne, France

### Components

#### 1. Email Classifier AI
- Classification of business emails into French categories
- Language: Python 3.14+
- Framework: Flask
- License: MIT (see LICENSE.md)

#### 2. PDF Generator AI
- Automatic generation of business documents
- Supported formats: PDF
- License: MIT (see LICENSE.md)

#### 3. Excel Analyzer AI
- Data anomaly detection and suggestions
- Supports: CSV, Excel files
- License: MIT (see LICENSE.md)

### Third-Party Attributions

#### LLM Providers (not bundled, external APIs)
- **Groq**: https://groq.com (free tier for MVP)
  - Model: Mixtral 8x7B
  - Terms: https://groq.com/terms
  
- **Mistral AI**: https://mistral.ai
  - Model: Mistral Small
  - License: https://mistral.ai/legal/terms/

- **OpenAI**: https://openai.com
  - Model: GPT-4o mini (optional)
  - Terms: https://openai.com/terms

#### Open Source Dependencies
All dependencies listed in `requirements.txt` are used under their respective open-source licenses:
- Flask (BSD 3-Clause)
- Pydantic (MIT)
- pandas (BSD 3-Clause)
- numpy (BSD 3-Clause)
- reportlab (BSD)
- pytest (MIT)
- python-dotenv (BSD)
- requests (Apache 2.0)

Full license details: See each package's LICENSE file in site-packages.

### License

IA PME Suite is distributed under the **MIT License**.  
See `LICENSE.md` for full text.

### Data Processing

#### Privacy
- **Email Classifier**: Processes email content for classification only. No persistent storage by default.
- **PDF Generator**: Generates PDFs based on user input. No tracking.
- **Excel Analyzer**: Analyzes spreadsheet data. No data retention.

#### GDPR Compliance (EU)
- No personal data collected by demos
- Interactive demo (demos.html) runs 100% client-side
- User can delete data anytime by clearing browser cache
- For production deployment: See `SECURITY.md`

#### Data Retention
- Demo data: Not stored
- Production data: Per user/customer contract
- Logs: Anonymized, retained 90 days

### Trademarks & Branding

**"IA PME"** is a trademark of Rudy Willoquet.  
Usage restrictions: See `TERMS_OF_SERVICE.md`

### Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Open Source Contribution

Contributions welcome! Please see `CONTRIBUTING.md` for:
- Code of Conduct
- Development setup
- Contribution guidelines
- Pull request process

### Disclaimer on Third-Party Services

This project uses external LLM APIs (Groq, Mistral, OpenAI) which have their own:
- Terms of Service
- Privacy Policies
- Rate limits
- Pricing models

Users are responsible for:
- Understanding and accepting those ToS
- Managing API keys securely
- Monitoring usage and costs
- Complying with each provider's acceptable use policy

### Contact

For licensing inquiries, copyright questions, or legal concerns:  
Email: willoquetr@gmail.com

---

**Last Updated**: December 9, 2025  
**Version**: 1.0.0
